from django.shortcuts import render


# Create your views here.
# post-list 함수
from .models import Post


def posts_list_view(request):

    posts = Post.objects.order_by['-pk']

    context = {
        'posts': posts,
    }
    return render(request, 'posts/post-list.html', context)
