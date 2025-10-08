from django.urls import path
from courses import views as course_views  # point to course-related instructor views

app_name = 'instructor'

urlpatterns = [
    # Instructor Dashboard
    path('dashboard/', course_views.instructor_dashboard, name='instructor_dashboard'),

    # Courses
    path('courses/add/', course_views.add_course, name='add_course'),
    path('courses/<int:course_id>/', course_views.course_detail, name='course_detail'),
    path('courses/<int:course_id>/edit/', course_views.course_edit, name='course_edit'),

    # Lectures
    path('courses/<int:course_id>/add-lecture/', course_views.add_lecture, name='add_lecture'),

    # Feedback
    path('courses/<int:course_id>/feedback/', course_views.give_feedback, name='give_feedback'),

    path('courses/<int:course_id>/events/add/', course_views.add_event, name='add_event'),
]
