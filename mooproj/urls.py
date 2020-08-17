from django.urls import path
from mooproj import views

urlpatterns = [
    path('', views.index, name='home'),
    path('previous_cows', views.previous_cows, name='previouscows')
]