from django.urls import path

from . import views

urlpatterns = [
    path('', views.members_view, name='members-view'),
    path('login/', views.login_view, name='login'),
]