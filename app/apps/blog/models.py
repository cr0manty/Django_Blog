from django.db import models
from django.shortcuts import reverse
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

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = (slugify_url(self.title) + '-' + str(int(time())))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_create']


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
        if not self.id:
            self.slug = slugify_url(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    date_create = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.author

    class Meta:
        ordering = ['-date_create']
