from django.urls import path, include
from products import views


urlpatterns = [
    path('productcategory/', views.ProductCategoryList.as_view()),
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetails.as_view()),
]