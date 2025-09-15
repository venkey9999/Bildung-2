from django.urls import path
from . import views

urlpatterns = [
    path("<int:course_id>/", views.forum_list, name="forum_list"),
    path("<int:course_id>/new/", views.create_post, name="create_post"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
]
