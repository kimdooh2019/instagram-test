from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [

    path('', views.posts_list_view, name='posts-list'),
    path('<int:pk>/like/', views.post_like_view, name='post-like'),
    path('create/', views.post_create_view, name='post-create'),
    path('<int:post_pk>/comments/create/', views.comment_create, name='comment-create'),
]