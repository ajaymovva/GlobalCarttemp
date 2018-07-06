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


class Deleteitem(DeleteView):
    model = addtocart
    template_name = 'deleteform.html'
    success_url = reverse_lazy('GlobalCartapp:cartitems')
