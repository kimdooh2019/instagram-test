from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    img_profile = models.ImageField('프로필이미지', blank=True, upload_to='userssadf/')

    # username = models.CharField('아이디',rela, max_length=100)
    name =  models.CharField('이름', max_length=100)
    # password = models.CharField('비밀번호', max_length=100)
