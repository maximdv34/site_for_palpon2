from django.shortcuts import render

from .models import Post, Client


def index(request):
    return render(request, 'index.html', {'posts': Post.objects.order_by('-created_date'),
                                          'clients': Client.objects.order_by('-created_date')})


def blog(request):
    return render(request, 'blog.html', {'posts': Post.objects.order_by('-created_date')})
