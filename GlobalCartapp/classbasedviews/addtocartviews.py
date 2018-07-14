from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from GlobalCartapp.models import *
from django.shortcuts import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class cartlistview(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = addtocart
    context_object_name = 'object'
    template_name = "addtocartinfo.html"

    def get_queryset(self):
        user = self.request.user
        return addtocart.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super(cartlistview, self).get_context_data(**kwargs)
        context.update({'user_permissions': self.request.user.get_all_permissions()})
        userinfoid = userinfo.objects.get(user=self.request.user)
        context.update({'obj': userinfoid.id})
        return context


def addnewitem(request, pk):
    if request.user.is_authenticated:
        user = request.user
        item = Item.objects.get(id=pk)
        itemtocart = addtocart(user=user, item=item, price=item.price, image=item.image, quantity=1)
        itemtocart.save()
        return redirect('GlobalCartapp:cartitems')
    else:
        return redirect('GlobalCartapp:login')


def addexistitem(request, pk):
    if request.user.is_authenticated:
        user = request.user
        cart = addtocart.objects.get(id=pk)
        cart.quantity = cart.quantity + 1
        item = Item.objects.get(id=cart.item.id)
        cart.price = cart.price + item.price
        cart.save()
        return redirect('GlobalCartapp:cartitems')
    else:
        return redirect('GlobalCartapp:login')


class Deleteitem(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = addtocart
    template_name = 'deleteform.html'
    success_url = reverse_lazy('GlobalCartapp:cartitems')

    def has_permission(self):
        pk = self.kwargs['pk']
        user_id = self.request.user.id
        # import ipdb
        # ipdb.set_trace()
        check_user = addtocart.objects.get(pk=pk).user.id

        if not user_id == check_user:
            self.raise_exception = True
            success_url = reverse_lazy('GlobalCartapp:cartitems')
            return False
        else:
            def get(self, request, *args, **kwargs):
                return self.post(request, args, kwargs)

            success_url = reverse_lazy('GlobalCartapp:cartitems')
            return True


def cashondelivercart(request):
    return render(request, 'payment_successcart_cash.html')


def Bookitem(request):
    queryset = addtocart.objects.all()
    user = request.user
    for iter in queryset:
        if iter.user == user:
            bookobj = Bookedinfo(user=user, item=iter.item, price=iter.price, image=iter.image, quantity=1)
            bookobj.save()
    return redirect("GlobalCartapp:Bookeditems")
