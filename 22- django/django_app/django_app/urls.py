"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
# Import app
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', views.helloworld, name='helloworld'),
    path('', views.index, name='index'),
    path('index/', views.index, name='inicio'),
    path('test-page/', views.page, name='page'),
    path('test-page/<int:redirection>', views.page, name='page'),
    path('contact/', views.contact, name='contact'),
    path('contact/<str:name>', views.contact, name='contact')
]
