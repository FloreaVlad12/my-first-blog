from django import forms

from .models import Post, Comment, Event, Comment_event, Reply, Email

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)    
        
        
class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'manager', 'description',)    
        
class Comment_eventForm(forms.ModelForm):

    class Meta:
        model = Comment_event
        fields = ('author', 'text',)    
        
        
class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ('author', 'text',)   
        
        
class EmailForm(forms.ModelForm):

    class Meta:
        model = Email
        fields = ('subject', 'text', 'your_email',)                    