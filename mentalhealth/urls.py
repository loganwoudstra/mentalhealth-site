from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('newentry/', views.newentry, name="newentry"),
    path('allentries/', views.allentries, name="allentries"),
    path('<int:id>/', views.oldentry, name="oldentry"),
    path('delete/<int:id>/', views.del_entry, name="del_entry"),
    path('checkin/', views.checkin, name="checkin"),
    path('depression_detected/', views.depression_detected, name="depression_detected"),
    path('about_model/', views.about_model, name="about_model"),
]