from django.contrib import admin
from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
	
class ArticleAdmin(admin.ModelAdmin):
	list_display = ['title' , 'category' , 'author' , 'views']
	

	
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)	