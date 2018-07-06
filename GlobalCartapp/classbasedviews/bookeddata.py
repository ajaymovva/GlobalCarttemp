from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from GlobalCartapp.models import *
from django.shortcuts import *
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


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
        return render_to_response('payment success.html')
    else:
        return redirect('GlobalCartapp:login')
