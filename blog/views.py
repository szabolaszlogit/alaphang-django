from django.shortcuts import get_object_or_404, render

from .models import Post, Category

from django.views import View

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

class DetailView(View):
    

    q = Post(post_title="What's new?", post_category_id = 1, post_order = 33,  post_content = 'dhsdjsdjsadhhsh' )
    q.save()

