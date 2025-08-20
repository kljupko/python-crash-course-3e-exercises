from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Blog, Post
from .forms import BlogForm, PostForm

# Helper functions.
def check_blog_owner(blog, request):
    """Check if the blog belongs to the current user."""
    if blog.owner != request.user:
        raise Http404

# Create your views here.
def index(request):
    """The home page of the site."""
    posts = Post.objects.all().order_by('-date_added')

    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

def blog(request, blog_id):
    """Shows a blog."""
    blog = Blog.objects.get(id=blog_id)
    posts = blog.post_set.order_by('-date_added')

    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs/blog.html', context)

def post(request, post_id):
    """Shows a post."""
    post = Post.objects.get(id=post_id)
    blog = post.blog

    context = {'blog': blog, 'post': post}
    return render(request, 'blogs/post.html', context)

def blogs(request):
    """Shows all blogs."""
    blogs = Blog.objects.all().order_by('name')
    
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

@login_required
def new_blog(request):
    """Add a new blog."""
    if request.method != 'POST':
        # Create blank form.
        form = BlogForm()
    else:
        # Data sent for submission.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:blogs')
    
    # Display blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

@login_required
def new_post(request, blog_id):
    """Add a new post for a particular blog."""
    blog = Blog.objects.get(id=blog_id)
    check_blog_owner(blog, request)

    if request.method != 'POST':
        # Create blank form.
        form = PostForm()
    else:
        # Data sent for submission.
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect('blogs:blog', blog_id=blog_id)
    
    # Display a blank or invalid form.
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Edit an existing post."""
    post = Post.objects.get(id=post_id)
    blog = post.blog
    check_blog_owner(blog, request)

    if request.method != 'POST':
        # Pre-fill with current data.
        form = PostForm(instance=post)
    else:
        # Data sent for submission.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog.id)
    
    # Display a blank or invalid form.
    context = {'post': post, 'blog':blog, 'form': form}
    return render(request, 'blogs/edit_post.html', context)