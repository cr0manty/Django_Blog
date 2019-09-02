from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from slugify import slugify_url
from time import time


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_create = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_edit_url(self):
        return reverse('post_edit_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def get_comment_add_url(self):
        return reverse('add_comment_url', kwargs={'slug': self.slug})

    def add_author(self, new_author):
        self.author = new_author

    def save(self, *args, **kwargs):
        self.slug = (slugify_url(self.title) + '-' + str(int(time())))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_create']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Tag(models.Model):
    title = models.CharField(max_length=25, unique=True)
    slug = models.SlugField(blank=True, unique=True)

    def get_absolute_url(self):
        return reverse('tags_detail_url', kwargs={'slug': self.slug})

    def get_edit_url(self):
        return reverse('tag_edit_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify_url(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    is_edit = models.BooleanField(default=False)

    def get_comment_delete_url(self):
        return reverse('comment_delete_url', kwargs={
            'id': self.id,
            'slug': self.post.slug
        })

    class Meta:
        ordering = ['-date_create']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'
