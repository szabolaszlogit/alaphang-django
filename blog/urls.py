from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    
    #path('<int:post_order>/', views.DetailView, name='detail'),#
    path('page/<slug:slug>/', views.PageDetailView.as_view(), name='page'),
    path('category/<slug:slug>/', views.Categorys.as_view(), name='categorys'),
    path('<slug:slug>/', views.SlugDetailView.as_view(), name='detail'),
]