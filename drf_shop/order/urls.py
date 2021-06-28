
from django.urls import path
#from .views import checkout, OrdersList
from order import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('orders/', views.OrdersList.as_view()),
]