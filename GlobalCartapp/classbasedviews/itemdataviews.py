from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from GlobalCartapp.forms.Itemforms import *
from django.urls import reverse_lazy
from django.shortcuts import render
from django.shortcuts import *


class AllItemlistview(ListView):
    model = Item
    context_object_name = 'object'
    template_name = "itemdetails.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AllItemlistview, self).get_context_data(**kwargs)
        context['data'] = self.model.objects.all()
        context.update({'user_permissions': self.request.user.get_all_permissions()})
        return context


def filteritems(request, category):
    object = Item.objects.filter(category=category)
    return render(request, 'itemdetails.html', {'object': object})


class CreateItemview(CreateView):
    model = Item
    context_object_name = 'object'
    template_name = 'item_forms.html'
    form_class = AddItem
    success_url = reverse_lazy('GlobalCartapp:items')


class EditItemsview(UpdateView):
    model = Item
    context_object_name = 'object'
    template_name = "item_forms.html"
    form_class = AddItem
    success_url = reverse_lazy('GlobalCartapp:items')


class DeleteItemView(DeleteView):
    model = Item
    context_object_name = 'object'
    form_class = AddItem
    success_url = reverse_lazy('GlobalCartapp:items')

    def get(self, request, *args, **kwargs):
        return self.post(request, args, kwargs)


def search(request):
    object = Item.objects.all()
    searchitem = request.GET['item']
    listofid = []
    for i in object:
        print(i.name)
        if searchitem in i.name:
            listofid.append(i.id)
    object1 = Item.objects.filter(id__in=listofid)
    print(object1)
    return render(request, 'searchitems.html', {'object': object1})


class Itemreviewscreate(CreateView):
    model = Itemreviews
    form_class = ReviewratingForm
    template_name = 'itemreview_form.html'

    def post(self, request, *args, **kwargs):
        reviewobj = ReviewratingForm(request.POST)
        if reviewobj.is_valid():
            reviewobj = reviewobj.save(commit=False)
            reviewobj.user = self.request.user
            item = Item.objects.get(id=kwargs['pk'])
            reviewobj.item = item
            reviewobj.save()
        return redirect('GlobalCartapp:itemcompleteinfo', pk=kwargs['pk'])


class Paymentdone(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payment_form.html'

    def post(self, request, *args, **kwargs):
        payment = PaymentForm(request.POST)
        if payment.is_valid():
            paymentobj = payment.save(commit=False)
            paymentobj.user = self.request.user
            item = Item.objects.get(id=kwargs['pk'])
            paymentobj.item = item
            paymentobj.save()
        return redirect('GlobalCartapp:Bookitem', pk=kwargs['pk'])


def itemdetailinfo(request, pk):
    if request.user.is_authenticated:
        object = Item.objects.get(id=pk)
        coments = Itemreviews.objects.values('user__username', 'rating', 'reviews').filter(item=object)
        return render(request, 'itemdisplay.html', {'object': object, 'review': coments})
    else:
        return redirect('GlobalCartapp:login')
