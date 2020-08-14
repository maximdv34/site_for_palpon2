from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.detail, name='detail'),
    path('auto_in_vendita/', views.auto_in_vendita, name='auto_in_vendita'),
    path('presentiamoci/', views.presentiamoci, name='presentiamoci'),
    path('entra_in_contatto/', views.entra_in_contatto, name='entra_in_contatto'),
    path('paga_con_comodo/', views.paga_con_comodo, name='paga_con_comodo'),
    path('perche_noi/', views.perche_noi, name='perche_noi'),
    path('reviews/', views.reviews, name='reviews'),
    path('valutazione', views.valutazione, name='valutazione'),
]

