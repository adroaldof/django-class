from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse

from .forms import PostForm
from .models import Post


def index(request):
    ''' Show index page '''
    return render(request, 'index.html')


def create_post(request):
    print('asdfasd')
    ''' Create a new post '''
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.like = 0
            try:
                post.save()
                return redirect(reverse('blog:list'))
            except Exception as e:
                print e
    else:
        form = PostForm()

    return render(request, 'create_post.html', {
        'form': form
    })


def list_posts(request):
    ''' List all posts '''
    posts = Post.objects.all()

    return render(request, 'posts.html', {
        'posts': posts
    })


def update_post(request, post_id):
    ''' Update an existing post '''
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            try:
                post.save()
                return redirect(reverse('blog:list'))
            except Exception as e:
                print e
    else:
        form = PostForm(instance=post)

    return render(request, 'create_post.html', {
        'post': post
    })


def view_post(request, post_id):
    ''' View an existing post '''
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'post.html', {
        'post': post
    })


def delete_post(request, post_id):
    ''' Delete an existing post '''
    pass

