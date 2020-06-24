from django.shortcuts import get_object_or_404, render

from .models import Post, Category

from django.views import View
from django.views import generic

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

            nextpost = Post.objects.get(post_order=self.object.post_order+1)
            if Post.objects.filter(pk = nextpost.pk).exists():
                context['next'] = Post.objects.get(post_order=self.object.post_order+1)
            else:
                context['next'] = None

   
            #context['next'] = Post.objects.get(pk=self.object.post_order+1)
            #context['prev'] = Post.objects.get(pk=self.object.post_order-1)
            context['categorys'] = Category.objects.all()
            context['posts_in_actual_category'] = Post.objects.filter(post_category=self.object.post_category)
            return context

class Posts(generic.ListView):
    model = Post