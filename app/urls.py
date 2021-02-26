from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('produtoInfo', views.produtoInfo, name='produtoInfo'),
    path('sobreNos', views.sobreNos, name='sobreNos')
]