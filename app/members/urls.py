from django.urls import path

from . import views

app_name = 'members'

urlpatterns = [
    path('', views.members_view, name='members-view'),
    path('login/', views.login_view, name='login'),
    # path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

]