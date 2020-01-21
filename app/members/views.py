from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

# from .models import User
from .forms import LoginForm, SignupForm

User = get_user_model()


def members_view(request):
    return render(request, 'members/index.html')


def login_view(request):
    if request.method == 'POST':
        # username = request.POST['username']
        # password = request.POST['password']
        # user = authenticate(request, username=username, password=password)
        # # user는 username 반환
        # print('user: ', user)
        # if user:
        #     login(request, user)
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('posts:posts-list')

    else:
        form = LoginForm()
        print(form)

    context = {
        'form': form,
    }
    return render(request, 'members/login.html', context)


def signup_view(request):
    """
    Template: index.html을 그대로 사용
        action만 이쪽으로
    URL: /members/signup/
    User에 name필드를 추가
        email
        username
        name
        password
    를 전달받아, 새로운 User를 생성한다
    생성시, User.objects.create_user() 메서드를 사용한다
    이미 존재하는 username또는 email을 입력한 경우,
    "이미 사용중인 username/email입니다" 라는 메시지를 HttpResponse로 돌려준다
    생성에 성공하면 로그인 처리 후 (위의 login_view를 참조) posts:post-list로 redirect처리
    :param request:
    :return:
    """
    # email = request.POST['email']
    # username = request.POST['username']
    # name = request.POST['name']
    # password = request.POST['password']
    #
    # if User.objects.filter(username=username).exists():
    #     return HttpResponse('이미 사용중인 username입니다')
    # if User.objects.filter(email=email).exists():
    #     return HttpResponse('이미 사용중인 email입니다')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:post-list')
    else:
        form = SignupForm()


    # user = User.objects.create_user(
    #     password=password,
    #     username=username,
    #     email=email,
    #     name=name,
    # )
    # login(request, user)
    context = {
        'form' : form,
    }
    return render(request, 'members/signup.html', context)

def logout_view(request):
    # GET 요청으로 처리함

    logout(request)
    return redirect('members:login')

    # Template: index.html을 그대로 사용
    #     action만 이쪽으로
    # URL: /members/signup/
    # Form: members.forms.SignupForm
    # User에 name필드를 추가
    #     email
