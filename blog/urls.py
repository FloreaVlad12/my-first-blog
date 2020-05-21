from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('kr', views.kr_post_list, name='kr_post_list'),
    path('post/<int:pk>/kr', views.kr_post_detail, name='kr_post_detail'),
    path('post/<int:pk>/edit/kr', views.kr_post_edit, name='kr_post_edit'),
    path('post/<pk>/remove/kr', views.kr_post_remove, name='kr_post_remove'),
    path('post/<int:pk>/comment/kr', views.kr_add_comment_to_post, name='kr_add_comment_to_post'),
    path('comment/<int:pk>/remove/kr', views.kr_comment_remove, name='kr_comment_remove'),
    path('comment/<int:pk>/approve/kr', views.kr_comment_approve, name='kr_comment_approve'),
    path('post/new/kr', views.kr_post_new, name='kr_post_new'),
    path('post/<pk>/publish/kr', views.kr_post_publish, name='kr_post_publish'),
    path('drafts/kr', views.kr_post_draft_list, name='kr_post_draft_list'),
    
]