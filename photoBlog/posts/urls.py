from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),  
    path('post/<int:post_id>/edit/', views.post_update, name='post_update'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
] 