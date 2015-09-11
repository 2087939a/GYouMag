from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from app.models import Category, Article
from django.template.defaultfilters import slugify
from app.forms import ArticleForm


# Create your views here.


def index(request):
    article_list = Article.objects.all
    category_list = Category.objects.all
    trending_news = Article.objects.order_by('-views')
    latest_news = Article.objects.order_by('-pub_date')
    context_dict = {'categories' : category_list, 'articles' : article_list, 'latest': latest_news, 'trending' : trending_news }
    return render(request, 'app/index.html' , context_dict)

def about(request):
    article_list = Article.objects.all
    category_list = Category.objects.all
    latest_news = Article.objects.order_by('-pub_date')
    
    context_dict = {'categories' : category_list, 'articles' : article_list, 'latest': latest_news}
    return render(request, 'app/about.html' , context_dict)


def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        category_list = Category.objects.all
        context_dict['categories'] = category_list
        context_dict['category'] = category
        articles = Article.objects.filter(category=category)
        context_dict['articles'] = articles
        trending_news = Article.objects.filter(category = category).order_by('-views')
        latest_news_cat = trending_news.order_by('-pub_date')[:3]
        latest_news = Article.objects.order_by('-pub_date')
        context_dict['latest'] = latest_news
        context_dict['latest_cat'] = latest_news_cat
        context_dict['trending'] = trending_news
        
    except Category.DoesNotExist:

        pass

    
    return render(request, 'app/category.html', context_dict)





def article(request, article_title_slug, category_name_slug):
    context_dict = {}
  
  
    try:
        
        article = Article.objects.get(slug=article_title_slug)
        article.views += 1
        article.save()
        category = Category.objects.get(slug=category_name_slug)
        category_list = Category.objects.all
        latest_news = Article.objects.order_by('-pub_date')
        latest_news_cat = Article.objects.filter(category = category).order_by('-views').order_by('-pub_date')[:3]
        context_dict['latest'] = latest_news
        context_dict['latest_cat'] = latest_news_cat
        context_dict['categories'] = category_list
        context_dict['category_name'] = category.name
        context_dict['article_title'] = article.title
        context_dict['other_articles'] = Article.objects.filter(category=category)
        context_dict['article_content'] = article.content
        context_dict['article-image'] = article.image
        
    
    except Article.DoesNotExist:

        pass
    
    
    return render(request, 'app/article.html', context_dict)



def add_article(request, category_name_slug):

    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
                cat = None

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            if cat:
                article = form.save(commit=False)
                article.category = cat
                article.views = 0
                article.save()
                # probably better to use a redirect here.
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = ArticleForm()

    context_dict = {'form':form, 'category': cat}

    return render(request, 'app/add_article.html', context_dict)