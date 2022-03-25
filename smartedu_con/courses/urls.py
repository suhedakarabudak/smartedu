from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import views

#tek tek sayfaları girmek için 9.satır
urlpatterns = [
    path('',views.course_list, name="courses"),
    path('<slug:category_slug>/<int:course_id>',views.course_detail, name="detail"),
    
] 