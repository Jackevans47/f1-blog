from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from .models import Post, Comment, Like, User
from .forms import CommentForm, EditProfileForm, PasswordChangingForm


# Create your views here.
class UserEditForm(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "account/edit_profile.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 3


def post_detail(request, slug):
    """
    Display an individual model :model:`blog.Post`.
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Comment submitted and awaiting approval",
            )

    comment_form = CommentForm()

    comment_data = []

    for comment in comments:
        likes = comment.likes
        # make a list of all the user ids that are on the likes
        # check if the request.user_id is in the list (get True/False)
        comment_data.append(
            {
                "id": comment.id,
                "author": comment.author,
                "body": comment.body,
                "approved": comment.approved,
                "created_on": comment.created_on,
                "like_count": comment.likes.count(),
                # "has_liked": True/False
            }
        )

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "coder": "Jack Evans",
            "comments": comment_data,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(
                request, messages.ERROR, "Error updating comment!"
            )

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))


def comment_like(request, slug, comment_id):
    """
    view to like a comment
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    user = get_object_or_404(User, pk=request.user.id)
    like = Like(user=user, comment=comment)
    like.save()

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    # success_url = reverse_lazy("home")
    success_url = reverse_lazy("password_success")


def password_success(request):
    return render(request, "account/password_success.html", {})
