"""GYou_Mag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns ,include, url
from django.contrib import admin
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
        url(r'^$', views.index, name='index'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/(?P<article_title_slug>[\w\-]+)/$', views.article, name='article'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_article/$', views.add_article, name='add_article'),
        url(r'^about/$', views.about, name='about'),

        )

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)






if not settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}),
        )

