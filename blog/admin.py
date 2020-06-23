from django.contrib import admin
# Register your models here.

from .models import Post, Category
from django.db.models import F

def post_order_increase(modeladmin, request, queryset):
    queryset.update(post_order=F('post_order')+1)    

post_order_increase.short_description = "Post order +1"


class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'post_published','post_category', 'post_order','post_show_in_navbar', 'slug' ]
    prepopulated_fields = {"slug": ("post_title",) }
    ordering = ['post_title']
    actions = [post_order_increase]
    list_filter = ('post_category', 'post_published', 'post_show_in_navbar')
    search_fields = ['post_title']
    list_editable = ['post_published','post_category', 'post_order', 'post_show_in_navbar']
admin.site.register(Post, PostAdmin)
admin.site.register(Category)