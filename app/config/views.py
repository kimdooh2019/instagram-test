from django.shortcuts import render, redirect


def index(request):
    # if request.POST['']
    if request.user.is_authenticated:
        return redirect('posts:posts.html')
    return render(request, 'index.html')
