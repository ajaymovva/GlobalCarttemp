from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from GlobalCartapp.models import *
from django.shortcuts import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class preorderlistview(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = preorder
    context_object_name = 'object'
    template_name = "preorderinfo.html"

    def get_queryset(self):
        user = self.request.user
        return preorder.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super(preorderlistview, self).get_context_data(**kwargs)
        context.update({'user_permissions': self.request.user.get_all_permissions()})
        return context


def addpreorderitem(request, pk):
    if request.user.is_authenticated:
        user = request.user
        item = Item.objects.get(id=pk)
        itemtocart = preorder(user=user, item=item, price=item.price, image=item.image)
        itemtocart.save()
        return redirect('GlobalCartapp:preorderitems')
    else:
        return redirect('GlobalCartapp:login')


class Deletepreorderitem(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = preorder
    template_name = 'deleteform.html'
    success_url = reverse_lazy('GlobalCartapp:preorderitems')

    def has_permission(self):
        pk = self.kwargs['pk']
        user_id = self.request.user.id
        # import ipdb
        # ipdb.set_trace()
        check_user = preorder.objects.get(pk=pk).user.id

        if not user_id == check_user:
            self.raise_exception = True
            success_url = reverse_lazy('GlobalCartapp:preorderitems')
            return False
        else:
            def get(self, request, *args, **kwargs):
                return self.post(request, args, kwargs)

            success_url = reverse_lazy('GlobalCartapp:preorderitems')
            return True
