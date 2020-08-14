from django.shortcuts import render
from .models import Post, Client, Images


def index(request):
    return render(request, 'index.html', {'posts': Post.objects.order_by('-created_date'),
                                          'clients': list(Client.objects.order_by('-created_date'))})


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    images = list(Images.objects.filter(post=pk))
    return render(request, 'detail.html', {'post': post, 'images': images})


def auto_in_vendita(request):
    return render(request, 'auto_in_vendita.html', {'posts': Post.objects.order_by('-created_date')})


def entra_in_contatto(request):
    return render(request, 'entra_in_contatto.html')


def paga_con_comodo(request):
    return render(request, 'paga_con_comodo.html')


def perche_noi(request):
    return render(request, 'perche_noi.html')


def presentiamoci(request):
    return render(request, 'presentiamoci.html')


def valutazione(request):
    return render(request, 'valutazione.html')


def reviews(request):
    return render(request, 'reviews.html', {'clients': list(Client.objects.order_by('-created_date'))})