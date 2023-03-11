
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("post", views.post, name="post"),
    path("individual/<int:id>", views.individual, name="individual"),
    path("follow/<int:id>", views.follow, name="follow"),
    path("following_page", views.following_page, name="following_page")
]
