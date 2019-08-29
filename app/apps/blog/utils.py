from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Post, Tag
from django.http import Http404


def get_posts_pages(request):
    search = request.GET.get('search', '')
    posts = Post.objects.filter(
        Q(title__icontains=search) | Q(body__icontains=search)
    ) if search \
        else Post.objects.all()

    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    return page


def get_comments_pages(request, comments):
    paginator = Paginator(comments, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    return page


def get_pages_context(page):
    have_pages = page.has_other_pages()
    prev_url = '?page={}'.format(page.previous_page_number()) \
        if page.has_previous() else ''
    next_url = '?page={}'.format(page.next_page_number()) \
        if page.has_next() else ''

    return {
        'page': page,
        'have_pages': have_pages,
        'next_url': next_url,
        'prev_url': prev_url
    }


class ShowPostMixin:
    model = None
    template = None
    form_comment = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        context = {
            self.model.__name__.lower(): obj,
            'admin_object': obj,
            'form': self.form_comment(),
            'detail': True
        }
        page = get_comments_pages(request, obj.comment_set.all())
        context.update(get_pages_context(page))
        return render(request, self.template, context=context)


class CreateMixin:
    model = None
    template = None

    def get(self, request):
        return render(request, self.template, context={
            'form': self.model()}
                      )

    def post(self, request):
        obj = self.model(request.POST)
        if obj.is_valid():
            return redirect(obj.save())
        return render(request, self.template, context={
            'form': obj}
                      )


class EditMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        form = self.model_form(instance=obj)
        return render(request, self.template, context={
            'form': form,
            self.model.__name__.lower(): obj}
                      )

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        form = self.model_form(request.POST, instance=obj)
        if form.is_valid():
            return redirect(form.save())
        return render(request, self.template, context={
            'form': form,
            self.model.__name__.lower(): obj}
                      )


class DeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        raise Http404

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
