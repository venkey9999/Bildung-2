from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('create/', views.create_course, name='create_course'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('<int:course_id>/add-lecture/', views.add_lecture, name='add_lecture'),
    path('<int:course_id>/enroll/', views.enroll_course, name='enroll_course'),
    path('lecture/<int:lecture_id>/complete/', views.mark_lecture_complete, name='mark_lecture_complete'),
    path('<int:course_id>/progress-report/', views.course_progress_report, name='course_progress_report'),
    path('<int:course_id>/feedback/', views.give_feedback, name='give_feedback'),

    # New for events
    path('<int:course_id>/add-event/', views.add_event, name='add_event'),

    path('lecture/<int:lecture_id>/complete/', views.mark_lecture_complete, name='mark_lecture_complete'),
    path('student/dashboard/', user_views.student_dashboard, name='student_dashboard'),
    path('student/courses/', views.browse_courses, name='browse_courses'),
    path('student/enroll/<int:course_id>/', views.enroll_in_course, name='enroll_in_course'),
    path('student/course/<int:course_id>/', views.student_course_detail, name='student_course_detail'),
]

