from django.urls import path, include
from user import views


urlpatterns = [
    path('coustmer/', views.CoustmerList.as_view()),
    path('coustmer/<int:pk>/', views.CoustmerDetails.as_view()),

]