from django.contrib import admin
from django.urls import path, include

#to change the text at admin page
from index import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('cases', views.cases, name='cases'),
    path('contact', views.contact, name='contact'),

    
]

admin.site.site_header = "Siddhant admin page"
admin.site.site_title = "Welcome to Covid-19 overall admin page"
admin.site.index_title = "Welcome to Covid-19 grand website admin page"




















































































































































































































































