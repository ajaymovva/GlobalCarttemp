from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from GlobalCartapp.models import *
from django.shortcuts import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class wishlistview(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = wishlist
    context_object_name = 'object'
    template_name = "wishlistinfo.html"

    def get_queryset(self):
        user = self.request.user
        return wishlist.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super(wishlistview, self).get_context_data(**kwargs)
        context.update({'user_permissions': self.request.user.get_all_permissions()})
        return context


def addnewwishitem(request, pk):
    if request.user.is_authenticated:
        user = request.user
        item = Item.objects.get(id=pk)
        itemtocart = wishlist(user=user, item=item, price=item.price, image=item.image)
        itemtocart.save()
        return redirect('GlobalCartapp:wishlistitems')
    else:
        return redirect('GlobalCartapp:login')


class Deletewishlistitem(DeleteView):
    model = wishlist
    template_name = 'deleteform.html'
    success_url = reverse_lazy('GlobalCartapp:wishlistitems')
