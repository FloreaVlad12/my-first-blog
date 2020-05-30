from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models import Count


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True) 
    priority = models.PositiveSmallIntegerField(default=5)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    
    
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    #event= models.ForeignKey('blog.Event', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text    
    
    
class Event(models.Model):
     name = models.CharField('Event Name', max_length=120)
     event_date = models.DateTimeField('Event Date')
     venue = models.CharField(max_length=120)
     manager = models.CharField(max_length = 60)
     description = models.TextField(blank=True)
     
     def __str__(self):
         return self.name  
       
     def publish(self):
        self.save()
        
        
class Comment_event(models.Model):

    event= models.ForeignKey('blog.Event', on_delete=models.CASCADE, related_name='comment_events')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text   
    
    
class Reply(models.Model):

    comment_event= models.ForeignKey('blog.Comment_event', on_delete=models.CASCADE, related_name='replys')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text    
    
    
    
class Email(models.Model):

    subject = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    your_email = models.EmailField()

    def __str__(self):
        return self.text                