"""B6_Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django import views
from django.contrib import admin
# from django.urls import path
from django.urls import include, path #Video 111
#from book.views import homepage, show_all_books, edit_data
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('home/', homepage),
#     path('home/', homepage, name="homepage"), #after form submission move to homepage Time 26 Vidoe 109
#     path('show-all-books/', show_all_books, name="show_all_books"),
#     path('edit/', edit_data, name="edit"),
# ]


from book import views # same as above, imports all 3

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', homepage),
    path('home/', views.homepage, name="homepage"), #after form submission move to homepage Time 26 Vidoe 109
    path('show-all-books/', views.show_all_books, name="show_all_books"),
    path('edit/<int:id>', views.edit_data, name="edit"), 
    #instead of id, any name can be given
    #only this int: name must match with views functionn
    path('delete/<int:id>', views.delete_data, name="delete"), 

    #Video 111
    path('__debug__/', include('debug_toolbar.urls')),
    #Time 33:00, b6_env/Lib/site-packages/debug_toolbar


    #Assignment 8
    path('activate/<int:id>', views.activate_book, name="activate"), 
    path('deactivate/<int:id>', views.deactivate_book, name="deactivate"), 
    path('show_all_active_books/', views.show_all_active_books, name="show_active_books"),
    path('show_all_deactive_books/', views.show_all_deactive_books, name="show_deactive_books"),
    path('delete_all_books/', views.delete_all_books, name="delete_all"),
    path('activate_all_books/', views.activate_all_books, name="activate_all"),
    path('deactivate_all_books/', views.deactivate_all_books, name="deactivate_all"),
    
]