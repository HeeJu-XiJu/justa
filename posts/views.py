from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post, Comment

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)


def update(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else :
        form = PostForm(instance=post)
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)


def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('posts:index')


def comment_create(request,post_id):
    content = request.POST.get('comment')

    comment = Comment()
    comment.content = content
    comment.user_id = request.user.id
    comment.post_id = post_id
    comment.save()
    return redirect('posts:index')


def comment_delete(request, post_id, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('posts:index')