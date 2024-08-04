from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('add/', views.add_post, name='add_post'),
    path('tag/<str:tag_name>/', views.posts_by_tag, name='posts_by_tag'),
    path('post1/', views.post1, name='post1'),
    path('post2/', views.post2, name='post2'),
    path('post3/', views.post3, name='post3'),
    path('post4/', views.post4, name='post4'),
    path('post5/', views.post5, name='post5'),
    path('post6/', views.post6, name='post6'),
]