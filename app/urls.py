from nturl2path import url2pathname
from django.urls import URLPattern, path
from . import views

#create paths 
urlpatterns = [
    path('',views.store, name='store'),
    path('cart/',views.cart, name='cart'),
    path('checkout/',views.checkout, name='checkout'),
]