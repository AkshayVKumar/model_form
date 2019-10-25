"""P7 URL Configuration

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
from django.urls import path,include
from myapp import views
import myapp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('page1/',views.page1,name="page1"),
    path('page2/',views.page2,name="page2"),
    path('',include('myapp.urls')),
    path('create_topic/',views.create_topic,name='create_topic'),
    path('create_webpage/',views.create_webpage,name='create_webpage'),
    path('model_form/',views.Model_Form,name="modelform"),
]
#changing admin site
admin.site.site_header='OAR_Project'
admin.site.index_title='Django Class'
admin.site.site_title='OAR'