from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('publish_date_asc', views.post_list_publish_date_asc, name='post_list_publish_date_asc'),
    path('publish_date_desc', views.post_list_publish_date_desc, name='post_list_publish_date_desc'),
    path('publish_date_asc/kr', views.kr_post_list_publish_date_asc, name='kr_post_list_publish_date_asc'),
    path('publish_date_desc/kr', views.kr_post_list_publish_date_desc, name='kr_post_list_publish_date_desc'),
  
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
    path('event/new/', views.event_new, name='event_new'),
    path('events', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('event/<pk>/remove/', views.event_remove, name='event_remove'),
    path('event/<int:pk>/comment/', views.add_comment_to_event, name='add_comment_to_event'),
    path('event/<int:pk>/comment/reply', views.add_reply_to_comment, name='add_reply_to_comment'),
    path('event/new/kr', views.kr_event_new, name='kr_event_new'),
    path('events/kr', views.kr_event_list, name='kr_event_list'),
    path('event/<int:pk>/kr', views.kr_event_detail, name='kr_event_detail'),
    path('event/<int:pk>/edit/kr', views.kr_event_edit, name='kr_event_edit'),
    path('event/<pk>/remove/kr', views.kr_event_remove, name='kr_event_remove'),
    path('event/<int:pk>/comment/kr', views.kr_add_comment_to_event, name='kr_add_comment_to_event'),
    path('event/<int:pk>/comment/reply/kr', views.kr_add_reply_to_comment, name='kr_add_reply_to_comment'),
    path('contactus', views.contact, name='contact'),
    path('contactus/kr', views.kr_contact, name='kr_contact'),
    path('access_denied', views.no_permission, name='no_permission'),
    path('access_denied/kr', views.kr_no_permission, name='kr_no_permission'),
    path('picture/new', views.add_picture, name = 'add_picture'), 
    path('picture/<int:pk>/', views.picture_detail, name='picture_detail'),
    path('pictures', views.picture_list, name='picture_list'),
    path('picture/<pk>/remove/', views.picture_remove, name='picture_remove'),
    path('pictures/view-all', views.picture_list_view_all, name='picture_list_view_all'),
    path('picture/<pk>/like/', views.like_picture, name='like_picture'),
    path('picture/<pk>/unlike/', views.unlike_picture, name='unlike_picture'),
    
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 
