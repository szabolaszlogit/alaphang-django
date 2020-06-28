from django.shortcuts import get_object_or_404, render

from .models import Post, Category, Page

from django.views import View
from django.views import generic

def getPostNumber():
    postnumbers = {}
    for category in Category.objects.all():
        postnumbers[category.slug] = (Post.objects.filter(post_category=category).count())
    return postnumbers

def DetailView(request, post_order):
    post = get_object_or_404(Post, post_order=post_order)
    posts = Post.objects.all()
    navbars = Post.objects.filter(post_show_in_navbar = True)
    categorys = Category.objects.all()
    posts_in_category = Post.objects.filter(post_category = post.post_category)
    context = {
        'post': post,
        'posts': posts,
        'navbars': navbars,
        'categorys': categorys,
        'posts_in_category': posts_in_category
    }
    return render(request, 'blog/detail.html', context)


class SlugDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
           
            if Post.objects.filter(post_order = self.object.post_order+1).exists():
                context['next'] = Post.objects.get(post_order=self.object.post_order+1)
            else:
                context['next'] = None

            if Post.objects.filter(post_order = self.object.post_order-1).exists():
                context['prev'] = Post.objects.get(post_order=self.object.post_order-1)
            else:
                context['prev'] = None

            context['categorys'] = Category.objects.all()
            context['posts_in_actual_category'] = Post.objects.filter(post_category=self.object.post_category)
            context['navbars'] = Page.objects.all()

            return context

class PageDetailView(generic.DetailView):
    model = Page
    template_name = 'blog/page.html'
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)           
            context['categorys'] = Category.objects.all()
            context['navbars'] = Page.objects.all()
            return context

class Categorys(generic.ListView):
    model = Category
    template_name ='blog/category_list.html'
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)           
            context['categorys'] = Category.objects.all()
            context['navbars'] = Page.objects.all()
            context['posts'] = Post.objects.all()
            context['postnumbers'] = getPostNumber
            return context

class Posts(generic.ListView):
    model = Post