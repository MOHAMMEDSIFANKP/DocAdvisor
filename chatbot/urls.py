from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('review/', views.review_entry, name='review_entry'),
]