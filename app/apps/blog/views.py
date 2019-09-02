from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TagForm, PostForm, CommentForm
from .models import Comment
from .utils import *


class PostCreate(LoginRequiredMixin, CreateMixin, View):
    model = PostForm
    template = 'blog/post_create.html'
    raise_exception = True


class ShowPost(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        context = {
            'post': post,
            'admin_object': post,
            'form': CommentForm(),
            'detail': True
        }
        page = get_comments_pages(request, post.comment_set.all())
        context.update(get_pages_context(page))
        return render(request, 'blog/post.html', context=context)


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
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        context = {
            'tag': tag,
            'admin_object': tag,
            'detail': True
        }
        return render(request, 'blog/tag.html', context=context)


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
        form = CommentForm(request.POST)
        if form.is_valid():
            try:
                post.comment_set.create(
                    author=request.user,
                    text=form.cleaned_data.get('text')
                )
            except:
                return redirect(post.get_absolute_url())
            # TODO ошибка в случае ошибки
        return redirect(post.get_absolute_url())


class DeleteComment(View):
    def post(self, request, slug, id):
        comment = Comment.objects.get(id=id)
        comment.delete()
        return redirect('post_detail_url', slug=slug)


class EditComment(View):
    def post(self, request, slug, id):
        comment = Comment.objects.get(id=id)
        comment.is_edit = True
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
        return redirect('post_detail_url', slug=slug)
