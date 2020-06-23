from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    
    path('<int:post_order>/', views.DetailView, name='detail'),
    path('create/', views.Create, name='create'),
]