from django.contrib import admin
from .models import Post, Comment, Event, Comment_event, Reply

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Event)
admin.site.register(Comment_event)
admin.site.register(Reply)