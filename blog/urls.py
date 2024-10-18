from django.urls import path
from . import views
from .views import UserEditForm
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("edit_profile/", UserEditForm.as_view(), name="edit_profile"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path(
        "<slug:slug>/edit_comment/<int:comment_id>",
        views.comment_edit,
        name="comment_edit",
    ),
    path(
        "<slug:slug>/delete_comment/<int:comment_id>",
        views.comment_delete,
        name="c",
    ),
    path(
        "<slug:slug>/like_comment/<int:comment_id>",
        views.comment_like,
        name="comment_like",
    ),
]
