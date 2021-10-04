from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tipo_movto/', views.get_type_movto, name='Lista'),
    path('tipo_movto_id/<int:id>/', views.detail, name='Detalhes'),
]