from django.urls import path
from .views import category_list, post_list, post_detail, post_create, post_update, add_comment, edit_comment
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', category_list, name='category_list'),
    path('category/<int:category_id>/', post_list, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/new/', post_create, name='post_create'),
    path('post/<int:post_id>/edit/', post_update, name='post_update'),
    path('post/<int:post_id>/comment/', add_comment, name='add_comment'),
    path('comment/<int:comment_id>/edit/', edit_comment, name='edit_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
