from django.contrib import admin
from django.urls import path
from django_prj.views import main, burger_list, burger_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main), # main() 연결
    path('burgers/', burger_list), # burger_list() 연결
    path('search/', burger_search),
]

