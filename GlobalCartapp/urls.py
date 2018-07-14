from django.urls import path
from GlobalCartapp.classbasedviews.itemdataviews import *
from GlobalCartapp.classbasedviews.userinfoviews import *
from GlobalCartapp.classbasedviews.addtocartviews import *
from GlobalCartapp.classbasedviews.bookeddata import *
from GlobalCartapp.classbasedviews.wishlistviews import *
from GlobalCartapp.classbasedviews.preorderviews import *

app_name = "GlobalCartapp"

urlpatterns = [
    path(r'', homepage, name='home'),
    path('items/', AllItemlistview.as_view(), name="items"),
    path('items/<str:category>/', filteritems, name="itemsfilterdata"),
    path('itemsadd/', CreateItemview.as_view(), name='createitem'),
    path('items/<int:pk>/edit/', EditItemsview.as_view(), name='edititem'),
    path('items/<int:pk>/delete/', DeleteItemView.as_view(), name='deleteitem'),

    path('items/<int:pk>/ratings/', Itemreviewscreate.as_view(), name="reviews"),
    path('search/', search, name='searchitems'),

    path('items/<int:pk>/addtocart/', addnewitem, name='addtocart'),
    path('addtocart/', cartlistview.as_view(), name='cartitems'),
    path('items/<int:pk>/addtoexistcart/', addexistitem, name='addexistcart'),
    path('addtocart/<int:pk>/delete/', Deleteitem.as_view(), name='deletecartitem'),

    path('items/<int:pk>/wishlist/', addnewwishitem, name='addtowishlist'),
    path('wishlist/', wishlistview.as_view(), name='wishlistitems'),
    path('wishlist/<int:pk>/delete/', Deletewishlistitem.as_view(), name='deletewishitem'),

    path('items/<int:pk>/preorders/', addpreorderitem, name='addtopreorderlist'),
    path('preorders/', preorderlistview.as_view(), name='preorderitems'),
    path('preorders/<int:pk>/delete/', Deletepreorderitem.as_view(), name='deletepreorderitem'),

    path('items/<int:pk>/Bookeditem/', AddtoBookedList, name='Bookitem'),
    path('Bookitems/<int:pk>/delete/', DeleteBookitem.as_view(), name='deletebookitem'),
    path('items/<int:pk>/itemdetail/', itemdetailinfo, name='itemcompleteinfo'),
    path('items/<int:pk>/paymentform/', Paymentdone.as_view(), name='payment'),
    path('Bookitems/', BookeddataListview.as_view(), name='Bookeditems'),

    path('cartdeliver/', cashondelivercart, name='cashondelivercart'),
    path('cartbookitems/', Bookitem, name='cartbookitem'),
    path('cartuserinfo/<int:pk>/updatedetails', Updateuserinfocart.as_view(), name='updatecartprofile'),
    path('Bookcartitem/', Bookitem, name='Bookcart'),
    path('paymentcartform/', Paymentcartdone.as_view(), name='paymentcartdone'),

    path('item/<int:pk>/cashondelivary/', cashondelivary, name='cashondeliver'),
    path('item/<int:pk>/templaterender/', templatecashondeliver, name='templaterender'),
    path('contact/', contact, name='contact'),

    path('signup/', Createuserview.as_view(), name="signup"),
    path('user/<int:pk>/edituser/', Updateuser.as_view(), name='editprofile'),
    path('user/<int:pk>/edituserdetails/<int:itempk>/item', Updateuserinfo.as_view(), name="updateuserprofie"),
    path('userinfo/', userdetails, name='userdetails'),
    path("login/", LoginClass.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
]
