from django.urls import path
from .views import hello_spotify,RestaurantAPIView
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)



urlpatterns = router.urls

urlpatterns = [
    path('hello_spotify/', hello_spotify),
    path('restaurants/', RestaurantAPIView.as_view()),
    path('restaurants/<int:pk>/', RestaurantAPIView.as_view()),

]
