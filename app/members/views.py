from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def members_view(request):
    return render(request, 'members/index.html')


def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print('username :', username)
        print('password :', password)

        user = authenticate(request, username=username, password =password)
        print('user: ', user)
        if user:
            login(request, user)
            # config urls
            # path name=indexa 로 설정했는데 이것과 연관있는듯 하다다
            return redirect('indexa')

        else:
            return redirect('members:login')
    return render(request, 'members/login.html')
