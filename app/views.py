from django.shortcuts import get_object_or_404, redirect, render
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {'posts': posts}
    return render(request, 'home.html', context)

def post_detail(request, id):
    post = Post.objects.get(id=id)
    context = {'post': post}
    return render(request, 'post_detail.html', context)

def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('home')

# views.py
from django.shortcuts import render, redirect
from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


