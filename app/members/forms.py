from django import forms
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    # 로그인 시 사용
    # modle 구성
    username = forms.CharField(
        # html에서 input 만듬
        widget=forms.TextInput(
            # 속성 정의
            attrs={
                'class': 'form-control',
                'placeholder': '아이디',

            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호',
            }
        )
    )

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if not user:
            raise ValidationError('username or password 올바르지 않음')
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        login(request, user)


class SignupForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이메일',
            }
        )
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': '사용자명',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder': '비밀번호',
            }
        )
    )

    def clena(self):
        pass

    def save(self):
        """
        Form으로 전달받은 데이터를 사용해서
        새로운 User를 생성하고 리턴
        username과 email검증로직도 이 안에 넣기!
        """
        pass
