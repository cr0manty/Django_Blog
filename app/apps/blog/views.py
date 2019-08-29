from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TagForm, PostForm, CommentForm
from .utils import *


class PostCreate(LoginRequiredMixin, CreateMixin, View):
    model = PostForm
    template = 'blog/post_create.html'
    raise_exception = True


class ShowPost(ShowPostMixin, View):
    model = Post
    template = 'blog/post.html'
    form_comment = CommentForm


class EditPost(LoginRequiredMixin, EditMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_edit.html'
    raise_exception = True


class DeletePost(LoginRequiredMixin, DeleteMixin, View):
    model = Post
    redirect_url = 'blog_url'
    raise_exception = True


def show_posts(request):
    page = get_posts_pages(request)
    return render(request, 'blog/posts_list.html', context=get_pages_context(page))


class TagCreate(LoginRequiredMixin, CreateMixin, View):
    model = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class ShowTag(ShowPostMixin, View):
    model = Tag
    template = 'blog/tag.html'
    raise_exception = True


class EditTag(LoginRequiredMixin, EditMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_edit.html'
    raise_exception = True


class DeleteTag(LoginRequiredMixin, DeleteMixin, View):
    model = Tag
    redirect_url = 'tags_list_url'
    raise_exception = True


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class AddComment(View):
    def get(self, request, slug):
        raise Http404

    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        obj = CommentForm(request.POST)
        if obj.is_valid():
            post.comment_set.create(
                author=obj.cleaned_data.get('author'),
                text=obj.cleaned_data.get('text')
            )
            #TODO ошибка в случае ошибки
        return redirect(post.get_absolute_url())
