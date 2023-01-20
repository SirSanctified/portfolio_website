"""portfolio_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from portfolio_website import settings
from portfolio import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('contact/', views.ContactView.as_view()),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blogs/', views.blog_posts),
    path('blogs/<int:pk>/', views.blog_details),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
