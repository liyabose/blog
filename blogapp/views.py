from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm



from django.http import HttpResponse
def blog_list(request):
    posts = Blog.objects.all()
    return render(request, 'blogapp/blog_list.html', {'posts': posts})

def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blogapp/blog_form.html', {'form': form})

def blog_update(request, pk):
    post = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=post)
    return render(request, 'blogapp/blog_form.html', {'form': form})

def blog_delete(request, pk):
    post = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog_list')
    return render(request, 'blogapp/blog_delete.html', {'post': post})

def blog_detail(request, pk):
    post = Blog.objects.get(pk=pk)
    return render(request, 'blogapp/blog_detail.html', {'post': post})