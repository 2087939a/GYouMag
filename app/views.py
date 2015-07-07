from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from app.models import Category, Article


# Create your views here.


def index(request):
	
	category_list = Category.objects.all
	context_dict = {'categories' : category_list}
	
	return render(request, 'app/index.html' , context_dict)

def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:

        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        category_list = Category.objects.all
        context_dict['categories'] = category_list
        articles = Article.objects.filter(category=category)

        
        context_dict['articles'] = articles
        context_dict['category'] = category
    except Category.DoesNotExist:

        pass

    
    return render(request, 'app/category.html', context_dict)