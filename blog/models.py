from django.db import models

def defaultOrder():
    if Post.objects.all():
        return  Post.objects.order_by('-post_order')[0].post_order+1
    else:
        return 1

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    slug = models.SlugField()
    category_order = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.category_name

    class Meta:
        ordering = ["category_order"]

class Post(models.Model):
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=200)
    post_content = models.TextField()
    post_published = models.BooleanField(default=True)    
    post_order = models.PositiveSmallIntegerField(default=defaultOrder)
    slug = models.SlugField()

    def __str__(self):
        return self.post_title

    class Meta:
        ordering = ["post_order"]

class Page(models.Model):
    page_title = models.CharField(max_length = 200)
    page_content = models.TextField()
    slug = models.SlugField()
    page_order = models.PositiveSmallIntegerField()
    page_show_in_navbar= models.BooleanField(default=True)

    def __str__(self):
        return self.page_title

    class Meta:
        ordering = ["page_order"]