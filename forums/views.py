from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ForumPost, ForumReply
from courses.models import Course

@login_required
def forum_list(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    posts = course.forum_posts.all()
    return render(request, "forums/forum_list.html", {"course": course, "posts": posts})


@login_required
def create_post(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        ForumPost.objects.create(
            course=course,
            author=request.user,
            title=request.POST["title"],
            content=request.POST["content"],
        )
        return redirect("forum_list", course_id=course.id)
    return render(request, "forums/create_post.html", {"course": course})


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    if request.method == "POST":
        ForumReply.objects.create(
            post=post,
            author=request.user,
            content=request.POST["content"],
        )
        return redirect("post_detail", post_id=post.id)
    return render(request, "forums/post_detail.html", {"post": post})
