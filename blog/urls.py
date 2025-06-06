from django.urls import path
from . import views
urlpatterns = [
    path("", views.home_page, name="home"),
    path("posts", views.posts, name="posts_page"),
    path("posts/<slug:slug>", views.post_desc, name="detail_page")
]
