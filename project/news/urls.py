
from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
    path('', PostList.as_view(), name='posts' ),
    path('post_create/',  PostCreation.as_view(), name='post_create'),
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('author/<int:pk>/', AuthorDetail.as_view(), name='author_profile'),
    path('author/<int:pk>/edit/', AuthorUpdate.as_view(), name='author_update'),
]