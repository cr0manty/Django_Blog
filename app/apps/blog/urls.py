from django.urls import path
from .views import *

urlpatterns = [
    path('', show_posts, name='blog_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', ShowPost.as_view(), name='post_detail_url'),
    path('post/<str:slug>/edit', EditPost.as_view(), name='post_edit_url'),
    path('post/<str:slug>/delete', DeletePost.as_view(), name='post_delete_url'),
    path('tags/', tag_list, name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', ShowTag.as_view(), name='tags_detail_url'),
    path('tag/<str:slug>/edit', EditTag.as_view(), name='tag_edit_url'),
    path('tag/<str:slug>/delete', DeleteTag.as_view(), name='tag_delete_url')
]
