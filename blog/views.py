from django.shortcuts import render, redirect
from .models import Post, Comment, Event, Comment_event, Reply, Email, Picture
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm, EventForm, Comment_eventForm, ReplyForm, EmailForm, PictureForm
from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
from lib2to3.fixes.fix_input import context


# Create your views here.
def post_list(request):
     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-priority', '-published_date' )
     return render(request, 'blog/post_list.html', {'posts': posts})  
 
 
def post_list_publish_date_asc(request):
     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date' )
     return render(request, 'blog/post_list.html', {'posts': posts})   
 

def post_list_publish_date_desc(request):
     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date' )
     return render(request, 'blog/post_list.html', {'posts': posts})    
 
 
def kr_post_list_publish_date_asc(request):
     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date' )
     return render(request, 'blog/kr_post_list.html', {'posts': posts})   
 

def kr_post_list_publish_date_desc(request):
     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date' )
     return render(request, 'blog/kr_post_list.html', {'posts': posts})   





 

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
@permission_required('blog.change_post', '/access_denied' )
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
@permission_required('blog.delete_post', '/access_denied' )
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
@permission_required('blog.delete_comment', '/access_denied' )
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

def kr_post_list(request):
     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-priority', '-published_date' )
     return render(request, 'blog/kr_post_list.html', {'posts': posts})
 
def kr_post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/kr_post_detail.html', {'post': post})

@login_required
@permission_required('blog.change_post', '/access_denied/kr' )
def kr_post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('kr_post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/kr_post_edit.html', {'form': form})

@login_required
@permission_required('blog.delete_post', '/access_denied/kr' )
def kr_post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('kr_post_list')

def kr_add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('kr_post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/kr_add_comment_to_post.html', {'form': form})

@login_required
@permission_required('blog.delete_comment', '/access_denied/kr' )
def kr_comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('kr_post_detail', pk=comment.post.pk)

@login_required
def kr_comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('kr_post_detail', pk=comment.post.pk)

@login_required
def kr_post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('kr_post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/kr_post_edit.html', {'form': form})

@login_required
def kr_post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('kr_post_detail', pk=pk)

@login_required
def kr_post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/kr_post_draft_list.html', {'posts': posts})


def contact(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            #emai.author = request.user
            email.save()
            
            send_mail(
                       email.subject,
                       email.text,
                       email.your_email,
                       ['floreavlad2000@yahoo.com'],
                       fail_silently=True,
                     )
   
            return render(request, 'blog/thank_you_for_your_email.html')
    else:
        form = EmailForm()
    return render(request, 'blog/contact.html', {'form': form})




def kr_contact(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            #emai.author = request.user
            email.save()
            
            send_mail(
                       email.subject,
                       email.text,
                       email.your_email,
                       ['floreavlad2000@yahoo.com'],
                       fail_silently=True,
                     )
   
            return render(request, 'blog/kr_thank_you_for_your_email.html')
    else:
        form = EmailForm()
    return render(request, 'blog/kr_contact.html', {'form': form})



def no_permission(request):
    return render (request, 'blog/no_permission.html')

def kr_no_permission(request):
    return render (request, 'blog/kr_no_permission.html')


@login_required
@permission_required('blog.add_event', '/access_denied' )
def event_new(request):
   
      if request.method == "POST":
          form = EventForm(request.POST)
          if form.is_valid():
             event = form.save(commit=False)
             event.author = request.user
             event.save()
               
             return redirect('event_detail', pk=event.pk)
      else:
             form = EventForm()
             return render(request, 'blog/event_edit.html', {'form': form})
   

@login_required
@permission_required('blog.delete_event', '/access_denied' )
def event_remove(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('event_list')


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'blog/event_detail.html', {'event': event})

def event_list(request):
     #events = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
     events = Event.objects.filter().order_by('event_date')
     return render(request, 'blog/event_list.html', {'events': events})
 
@login_required
@permission_required('blog.change_event', '/access_denied' )
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'blog/event_edit.html', {'form': form}) 

def add_comment_to_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = Comment_eventForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.event = event
            comment.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = Comment_eventForm()
    return render(request, 'blog/add_comment_to_event.html', {'form': form})


def add_reply_to_comment(request, pk):
    comment_event = get_object_or_404(Comment_event, pk=pk)
    
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.comment_event = comment_event
            reply.save()
            return redirect('event_detail', pk=comment_event.event.pk)
            #return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = ReplyForm()
    return render(request, 'blog/add_reply_to_comment.html', {'form': form})






             #KR EVENT VIEWS-------------------------------
             
             
             
             
             
             
@login_required
@permission_required('blog.add_event', '/access_denied/kr' )
def kr_event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
   
            return redirect('kr_event_detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'blog/kr_event_edit.html', {'form': form})

@login_required
@permission_required('blog.delete_event', '/access_denied/kr' )
def kr_event_remove(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('kr_event_list')


def kr_event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'blog/kr_event_detail.html', {'event': event})

def kr_event_list(request):
     #events = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
     events = Event.objects.filter().order_by('event_date')
     return render(request, 'blog/kr_event_list.html', {'events': events})
 
@login_required
@permission_required('blog.delete_event', '/access_denied/kr' )
def kr_event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            
            return redirect('kr_event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'blog/kr_event_edit.html', {'form': form}) 

def kr_add_comment_to_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = Comment_eventForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.event = event
            comment.save()
            return redirect('kr_event_detail', pk=event.pk)
    else:
        form = Comment_eventForm()
    return render(request, 'blog/kr_add_comment_to_event.html', {'form': form})


def kr_add_reply_to_comment(request, pk):
    comment_event = get_object_or_404(Comment_event, pk=pk)
    
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.comment_event = comment_event
            reply.save()
            return redirect('kr_event_detail', pk=comment_event.event.pk)
            
    else:
        form = ReplyForm()
    return render(request, 'blog/kr_add_reply_to_comment.html', {'form': form}) 


#-------------PICTURE----------------------------

@login_required
def add_picture(request): 
  
    if request.method == 'POST': 
        form = PictureForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            picture = form.save(commit=False)
            picture.author = request.user
            picture.save()
            return redirect('picture_detail', pk=picture.pk)
            
    else: 
        form = PictureForm() 
    return render(request, 'blog/picture_form.html', {'form' : form})    


def picture_detail(request, pk):
    picture = get_object_or_404(Picture, pk=pk)
    is_liked = False
    if picture.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {
        'is_liked': is_liked,
        }    
    return render(request, 'blog/picture_detail.html', {'picture': picture})


def picture_list(request):
     pictures = Picture.objects.filter().order_by('-created_date')
     return render(request, 'blog/picture_list.html', {'pictures': pictures})
 
def picture_list_view_all(request):
     pictures = Picture.objects.filter().order_by('-created_date')
     return render(request, 'blog/picture_list_view_all.html', {'pictures': pictures}) 
 
@login_required 
@permission_required('blog.delete_picture', '/access_denied' )
def picture_remove(request, pk):
    picture = get_object_or_404(Picture, pk=pk)
    picture.delete()
    return redirect('picture_list')

@login_required 
def like_picture(request, pk):
    picture = get_object_or_404(Picture, pk=pk)
    picture.likes.add(request.user)
    return redirect('picture_detail', pk=pk)
    
@login_required 
def unlike_picture(request, pk):
    picture = get_object_or_404(Picture, pk=pk)
    picture.likes.remove(request.user)
    return redirect('picture_detail', pk=pk)
         