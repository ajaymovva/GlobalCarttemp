from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView, View
from GlobalCartapp.forms.Itemforms import *
from django.shortcuts import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class Createuserview(CreateView):
    model = userinfo
    form_class = Adduserprofile
    template_name = 'user_forms.html'

    def get_context_data(self, **kwargs):
        context = super(Createuserview, self).get_context_data(**kwargs)
        test_form = Adduser()
        context.update(
            {
                'user_form': context.get('form'),
                'test_form': test_form,
            }
        )
        return context

    def post(self, request, *args, **kwargs):
        userform = Adduser(request.POST)
        userprofile = Adduserprofile(request.POST)

        if userform.is_valid():
            user1 = userform.save(commit=False)
            user1.set_password(user1.password)
            user1.save()

            if userprofile.is_valid():
                userpro = userprofile.save(commit=False)
                userpro.wallet = 0
                userpro.user = user1
                login(request, user1)
                userpro.save()

        return redirect("GlobalCartapp:items")


class Updateuser(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = userinfo
    form_class = Adduserprofile
    template_name = 'user_forms.html'

    def has_permission(self):
        pk = self.kwargs['pk']
        user_id = self.request.user.id
        # import ipdb
        # ipdb.set_trace()
        check_user = userinfo.objects.get(pk=pk).user.id
        if not user_id == check_user:
            self.raise_exception = True
            return False
        else:
            return True

    def get_context_data(self, **kwargs):
        context = super(Updateuser, self).get_context_data(**kwargs)
        user_form = context.get('userinfo')
        test_form = Adduser(instance=user_form.user)
        context.update({
            'user_form': context.get('form'),
            'test_form': test_form,
        })
        return context

    def post(self, request, *args, **kwargs):
        # user = self.request.user
        userdata = userinfo.objects.get(id=kwargs['pk'])
        userinfoform = Adduserprofile(request.POST, instance=userdata)
        userform = Adduser(request.POST, instance=userdata.user)
        userform1 = userform.save(commit=False)
        userform1.set_password(userform1.password)
        userinfoform.save()
        userform1.save()
        return redirect("GlobalCartapp:items")


class Updateuserinfo(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = userinfo
    form_class = Add_delivaryinfo
    template_name = 'userinfo_form.html'

    def has_permission(self):
        pk = self.kwargs['pk']
        user_id = self.request.user.id
        check_user = userinfo.objects.get(pk=pk).user.id
        if not user_id == check_user:
            self.raise_exception = True
            return False
        else:
            return True

    def post(self, request, *args, **kwargs):
        userdata = userinfo.objects.get(id=kwargs['pk'])
        userdataform = Add_delivaryinfo(request.POST, instance=userdata)
        userdataobj = userdataform.save(commit=False)
        userdataobj.save()
        # print(kwargs['itempk'])
        itemobj = Item.objects.get(id=kwargs['itempk'])
        return render(request, "payment_info.html", {'object': itemobj})


class Updateuserinfocart(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = userinfo
    form_class = Add_delivaryinfo
    template_name = 'userinfo_form.html'

    def has_permission(self):
        pk = self.kwargs['pk']
        user_id = self.request.user.id
        check_user = userinfo.objects.get(pk=pk).user.id
        if not user_id == check_user:
            self.raise_exception = True
            return False
        else:
            return True

    def post(self, request, *args, **kwargs):
        userdata = userinfo.objects.get(id=kwargs['pk'])
        userdataform = Add_delivaryinfo(request.POST, instance=userdata)
        userdataobj = userdataform.save(commit=False)
        userdataobj.save()
        queryset = addtocart.objects.filter(user=self.request.user)
        totalprice = 0
        for i in queryset:
            totalprice = totalprice + i.price

        return render(request, "payment_infocart.html", {'query': queryset, 'total': totalprice})


def userdetails(request):
    if request.user.is_authenticated:
        user = request.user
        userdata = User.objects.values('username', 'email').filter(id=user.id)
        if user.id != 1:
            userinfo_data = userinfo.objects.filter(user=user)
            user1 = userinfo.objects.get(user=user)
        else:
            userinfo_data = None
            user1 = None
        return render(request, 'userdetails.html',
                      {'userdata': userdata, 'userinfo_data': userinfo_data, 'user': user1})
    else:
        return redirect('GlobalCartapp:login')


def logout_user(request):
    logout(request)
    return redirect('GlobalCartapp:items')


class LoginClass(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            template_name = "loginform.html"
            form = Loginform()
            context = {'form': form, 'title': 'login'}
            return render(request, template_name, context)
        else:
            return redirect("GlobalCartapp:items")

    def post(self, request):
        form = Loginform(request.POST)
        if form.is_valid():
            # user = User.objects.create_user(**form.cleaned_data)
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect("GlobalCartapp:items")
            else:
                return redirect("errorpage.html")
        else:
            return redirect("GlobalCartapp:login")


def contact(request):
    return render(request, 'contact-details.html', {})
