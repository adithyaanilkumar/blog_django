from django.urls import path, include
from . import views

urlpatterns = [
    path('home/',views.home,name="blog_home"),
    path('about/',views.about,name="blog_about")

]
