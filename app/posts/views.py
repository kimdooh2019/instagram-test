from django.contrib.auth import logout
from django.shortcuts import render, redirect

# Create your views here.
# post-list 함수
from .forms import PostCreateForm, CommentCreateForm
from .models import Post, PostLike


def posts_list_view(request, tag=None):
    # typeError

    if tag is None:
        posts = Post.objects.order_by('-pk')
    else:
        posts = Post.objects.filter(tags__name__iexact=tag).order_by('-pk')
    comment_form = CommentCreateForm()
    print(comment_form)
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }
    return render(request, 'posts/post-list.html', context)


def post_like_view(request, pk):
    post = Post.objects.get(pk=pk)
    print(post)
    user = request.user
    print(user)

    post_like_qs = PostLike.objects.filter(post=post, author=user)

    print(post_like_qs)
    if post_like_qs.exists():
        post_like_qs.delete()
    else:
        PostLike.objects.create(post=post, author=user)

    return redirect('posts:posts-list')


def post_create_view(request):
    # post
    if request.method == 'POST':

        text = request.POST['text']
        images = request.FILES.getlist('image')
        # post 추가 했어 author 와 text 가지고
        post = Post.objects.create(
            author=request.user,
            content=text
        )
        # image주소 받아옴
        # 어던 Post에 image가 추가되었는가?
        # 추가된 post의 postimage를 create(image 주소를 추가)
        # class PostImage(models.Model):
        #     image = models.ImageField(upload_to='posts/images')
        #     post = models.ForeignKey(Post, on_delete=models.CASCADE)
        # foreingkey 걸
        for image in images:
            post.postimage_set.create(image=image)
        return redirect('posts:post-list')

    else:
        form = PostCreateForm()
        print(form)
        context = {
            'form': form,
        }
    return render(request, 'posts/post-create.html', context)


def comment_create(request, post_pk):
    if request.method == 'POST':
        # 어떤 Post 에 comment가 걸렸는가?
        post = Post.objects.get(pk=post_pk)
        # post 보낸 content 값 뽑아오기
        # content = request.POST['content']
        # # post 걸린 postcomment에 create한다. request.user 옵션,  content옶션을 가지고 추가한다.
        # post.postcomment_set.create(
        #     author=request.user,
        #     content=content,
        # )
        print(request.POST)
        print('---------------------')
        form = CommentCreateForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save(post=post, author=request.user)
        return redirect('posts:posts-list')
