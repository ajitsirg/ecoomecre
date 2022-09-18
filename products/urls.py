from django.urls import path, include
from products import views


urlpatterns = [
    path('productcategory/', views.ProductCategoryList.as_view()),
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetails.as_view()),
    path('order/', views.OrderList.as_view()),
    path('order/<int:pk>/', views.OrderDetails.as_view()),
    path('orderitem/', views.OrderItemList.as_view()),
    path('orderitem/<int:pk>/', views.OrderItemDetails.as_view()),
]