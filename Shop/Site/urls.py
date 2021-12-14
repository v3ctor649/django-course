from django.urls import path
from .import views

from django.conf import settings
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.main_page,name = 'main_page'),    #главная страница
    path('assortment',views.assortment,name = 'assortment'),   #показать категории товаров
    path('category/<int:category_id>',views.show_category,name = 'category'),   # товары одной категории
    path('cart',views.show_cart,name = 'cart'),  #корзина
    path('orders',views.show_orders,name = 'orders'),
    path('favourite',views.show_favourite,name = 'favourite'), #избранные товары
    path('add-or-delete',views.add_or_delete,name = 'add_or_delete'),   #добавление/удаление в корзину
    path('add-or-delete-favourite',views.add_or_delete_favourite,name ='add_or_delete_favourite'), #добавление/удаление в избранное
    path('del-from-cart',views.del_from_cart,name = 'del_from_cart'),   #в корзине
    path('clear-cart',views.clear_cart,name = 'clear_cart'),            #в корзине
    path('make-order',views.make_order,name = 'make_order'),
    path('login',views.MyLoginView.as_view(),name = 'login'),
    path('logout', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]
