# -*- coding: utf-8 -*-

from django.shortcuts import render
from blog.models import Post, Categories
from django.shortcuts import redirect
from blog.forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    categories = Categories.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'blog/blog.html', context)


def create_post(request):
    categories = Categories.objects.all()
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'categories': categories,
        'form': form,
    }
    return render(request, 'blog/create_post.html', context)


def edit_post(request, post_id):
    categories = Categories.objects.all()
    post = Post.objects.get(pk=post_id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'categories': categories,
        'form': form,
    }
    return render(request, 'blog/edit_post.html', context)


def delete_post(request, post_id):
    posts = Post.objects.all()
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('/')
