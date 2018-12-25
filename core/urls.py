from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShoppingCartList.as_view(), name='home'),
    path('ProductList/', views.ProductList.as_view(), name='products'),
    path('api/products/', views.Products.as_view()),
    path('api/cartlist/', views.Carts.as_view()),
    path('api/del/<int:id>', views.DeleteView.as_view()),
    path('Update/<int:id>', views.ProductList.as_view(), name='update')
]