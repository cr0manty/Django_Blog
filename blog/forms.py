from django import forms
from .models import Post, Tag
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Заголовок'
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be create')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique!')
        return new_slug


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('slug', 'title', 'body', 'tags')
        widgets = {
            'slug': forms.TextInput(attrs={'type': 'hidden'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

        labels = {
            'slug': '',
            'title': 'Заголовок',
            'body': 'Текст',
            'tags': 'Теги'
        }

        def clean_slug(self):
            new_slug = self.cleaned_data['slug'].lower()
            if new_slug == 'create':
                raise ValidationError('Slug may not be create')
            return new_slug