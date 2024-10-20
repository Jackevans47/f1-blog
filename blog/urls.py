from django.urls import path, include
from . import views
from .views import UserEditForm, PasswordChangeView, PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("edit_profile/", UserEditForm.as_view(), name="edit_profile"),
    path(
        "<int:uid>/password/",
        PasswordsChangeView.as_view(
            template_name="account/password_change.html"
        ),
    ),
    path("password_success", views.password_success, name="password_success"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path(
        "<slug:slug>/edit_comment/<int:comment_id>",
        views.comment_edit,
        name="comment_edit",
    ),
    path(
        "<slug:slug>/delete_comment/<int:comment_id>",
        views.comment_delete,
        name="comment_delete",
    ),
    path(
        "<slug:slug>/like_comment/<int:comment_id>",
        views.comment_like,
        name="comment_like",
    ),
]
