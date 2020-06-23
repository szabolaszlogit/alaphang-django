from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Post(models.Model):
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=200)
    post_content = models.TextField()
    post_published = models.BooleanField(default=True)
    post_show_in_navbar= models.BooleanField(default=False)
    post_order = models.PositiveSmallIntegerField()
    slug = models.SlugField()

    def __str__(self):
        return self.post_title

    class Meta:
        ordering = ["post_order"]