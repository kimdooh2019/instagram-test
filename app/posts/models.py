import re

from django.db import models

from members.models import User


class Post(models.Model):
    TAG_PATTERN = re.compile(r'#(\w+)')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    content_html = models.TextField(blank=True)
    like_user = models.ManyToManyField(
        User, through='PostLike', related_name='like_post_set',
    )
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(
        'Tag', verbose_name='해시태그 목록', related_name='posts', blank=True,
    )

    def __str__(self):
        return '{author} : {content}'.format(
            # author은 User을 참조하는데
            author=self.author.username,
            content=self.content,
        )

    def _save_html(self):
        """
        content속성의 값을 사용해서 해시태그에 해당하는 문자열을 a태그로 바꾸어 줌
        :return: 해시태그가 a태그로 변환된 HTML
        """
        self.content_html = re.sub(
            self.TAG_PATTERN,
            r'<a href="/explore/tags/\g<1>/">#\g<1></a>',
            self.content,
        )

    def _save_tags(self):
        """
        content에 포함된 해시태그 문자열 (ex: #Python)의 Tag들을 만들고,
        자신의 tags Many-to-many field에 추가한다
        """
        tag_name_list = re.findall(self.TAG_PATTERN, self.content)
        tags = [Tag.objects.get_or_create(name=tag_name)[0] for tag_name in tag_name_list]
        self.tags.set(tags)

    def save(self, *args, **kwargs):
        self._save_html()
        super().save(*args, **kwargs)
        self._save_tags()

class PostImage(models.Model):
    # 이렇게 설정만 하면 올라가는건가?
    image = models.ImageField(upload_to='posts/images')
    # post (N) - PostImage (M) 관계가 아닌가?
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class PostComment(models.Model):
    # post 같은 경우 M:N관계가 아닌가?
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # author(1) : PostComment(N-F)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()


class PostLike(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField('태그명', max_length=100)

    def __str__(self):
        return self.name
