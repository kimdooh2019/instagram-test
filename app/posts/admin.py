from django.contrib import admin

from posts.models import Post, PostImage, PostComment, PostLike, Tag


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 3


# 화면 위치 선정해주느 것인가??
class PostCommentInline(admin.TabularInline):
    model = PostComment
    # extra = 1 은 문슨의미 인가
    extra = 2


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # admin page에서 list page 에서 보여줄 field 설정
    list_display = ('author', 'content', 'created')
    # admin 페이지에서 상세정보 페이지 link 연결할 field
    list_display_links = ('author', 'content')
    # post 생성 페이지에서 추가될 것들
    inlines = [
        PostImageInline,
        PostCommentInline
    ]
    readonly_fields = ('tags',)


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass