"""NewCRM URL Configuration

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
from django.urls import path

from user import views 
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    # Path Parameters
    path('getuser/<name>/<id>', views.pathview, name='pathview'), 
    # Query Parameters 
    path('getuser/', views.qryview, name='qryview') ,
    # Body Parameters
    path("showform/", views.showform, name="showform"), 
    # Return the Form Data
    path("getform/", views.getform, name='getform'),
    ## Return the Form Data
]  