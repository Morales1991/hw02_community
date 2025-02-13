from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("group/<slug>", views.group_posts, name="posts_group"),
    path("new", views.new_post, name="new_post"),
]
