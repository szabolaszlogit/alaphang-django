from django.contrib import admin
# Register your models here.

from .models import Post, Category, Page
from django.db.models import F

def post_order_increase(modeladmin, request, queryset):
    queryset.update(post_order=F('post_order')+1)    

post_order_increase.short_description = "Post order +1"


class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'post_published','post_category', 'post_order', 'slug','pk' ]
    prepopulated_fields = {"slug": ("post_title",) }
    ordering = ['post_order']
    actions = [post_order_increase]
    list_filter = ('post_category', 'post_published')
    search_fields = ['post_title']
    list_editable = ['post_published','post_category', 'post_order']

class PageAdmin(admin.ModelAdmin):
    list_display = ['page_title', 'page_order', 'slug', 'page_show_in_navbar' ]
    prepopulated_fields = {"slug": ("page_title",) }
    ordering = ['page_order']
    list_editable = ['page_show_in_navbar', 'page_order']   

class CategoryAdmin(admin.ModelAdmin):
    list_display = [ 'category_name', 'slug']
    prepopulated_fields = {"slug": ("category_name",) }
 

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)