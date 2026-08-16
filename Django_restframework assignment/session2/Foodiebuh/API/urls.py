from django.urls import path
from .views import hello_spotify,RestaurantAPIView



urlpatterns = [
    path('hello_spotify/', hello_spotify),
    path('restaurants/', RestaurantAPIView.as_view()),
    path('restaurants/<int:pk>/', RestaurantAPIView.as_view()),
]
