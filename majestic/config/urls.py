"""Main URL Configuration file"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from .sitemap import StaticViewSitemap


sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('majestic.urls', namespace='majestic')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap-xml')
]
