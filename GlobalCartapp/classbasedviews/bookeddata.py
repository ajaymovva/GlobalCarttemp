from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from GlobalCartapp.models import *
from django.shortcuts import *
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy


class BookeddataListview(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Bookedinfo
    context_object_name = 'object'
    template_name = "Bookedinfo.html"

    def get_queryset(self):
        user = self.request.user
        return Bookedinfo.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super(BookeddataListview, self).get_context_data(**kwargs)
        context.update({'user_permissions': self.request.user.get_all_permissions()})
        return context


def AddtoBookedList(request, pk):
    if request.user.is_authenticated:
        user = request.user
        item = Item.objects.get(id=pk)
        bookeddata = Bookedinfo(user=user, item=item, price=item.price, image=item.image, quantity=1)
        bookeddata.save()
        itemname = item.name
        itemprice = item.price

        subject = 'GlobalCart order'
        message = """
            <html>
                <head>
                    <h2>Thankyou for purchasing from GlobalCart</h2>
                </head>
                <body>
                <table border="2">
                    <tr>
                    <td>Itemname:</td>
                    <td>""" + str(itemname) + """</td>
                    </tr>
                    <tr>
                    <td>ItemPrice:</td>
                    <td>""" + str(itemprice) + """</td>
                    </tr>
                </table>
                </body>
            </html>
        """
        # to_list = ['majaykumar51@gmail.com']
        # obj = EmailMessage(subject, message, settings.EMAIL_HOST_USER, to_list)
        # obj.content_subtype = "html"
        # obj.send()
        return redirect('GlobalCartapp:Bookeditems')
    else:
        return redirect('GlobalCartapp:login')


class DeleteBookitem(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    model = Bookedinfo
    template_name = 'deleteform.html'
    success_url = reverse_lazy('GlobalCartapp:Bookeditems')

    def has_permission(self):
        pk = self.kwargs['pk']
        user_id = self.request.user.id
        # import ipdb
        # ipdb.set_trace()
        check_user = Bookedinfo.objects.get(pk=pk).user.id

        if not user_id == check_user:
            self.raise_exception = True
            success_url = reverse_lazy('GlobalCartapp:Bookeditems')
            return False
        else:
            def get(self, request, *args, **kwargs):
                return self.post(request, args, kwargs)

            success_url = reverse_lazy('GlobalCartapp:Bookeditems')
            return True


def cashondelivary(request, pk):
    user = request.user
    userdetail = userinfo.objects.get(user=user)
    # import ipdb
    # ipdb.set_trace()
    return redirect('GlobalCartapp:updateuserprofie', userdetail.id, pk)


def templatecashondeliver(request, pk):
    return render(request, "payment_cashondeliver.html", {'pk': pk})
