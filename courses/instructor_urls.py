from django.urls import path
from courses import views

urlpatterns = [
    # Instructor Dashboard
    path('dashboard/', views.instructor_dashboard, name='instructor_dashboard'),

    # Instructor-only course management
    path('add-course/', views.add_course, name='add_course'),
    path('course/<int:course_id>/', views.course_detail, name='instructor_course_detail'),
    path('course/<int:course_id>/add-lecture/', views.add_lecture, name='add_lecture'),
    path('course/<int:course_id>/feedback/', views.give_feedback, name='give_feedback'),
]
