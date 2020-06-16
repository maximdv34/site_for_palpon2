from django.shortcuts import render

from .models import Post, Client


def index(request):
    # print(list(Post.objects.values('image', 'title')))
    return render(request, 'index.html', {'posts': Post.objects.order_by('created_date'),
                                          'clients': Client.objects.order_by('info')})


def blog(request):
    return render(request, 'blog.html', {'posts': Post.objects.order_by('created_date')})
