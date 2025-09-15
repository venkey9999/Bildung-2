from django.shortcuts import render, redirect, get_object_or_404
from courses.models import Course, Lecture, Enrollment, Feedback
from courses.forms import CourseForm, LectureForm, FeedbackForm
from django.contrib.auth.decorators import login_required

@login_required
def instructor_dashboard(request):
    courses = Course.objects.filter(instructor=request.user)
    return render(request, 'instructor/dashboard.html', {'courses': courses})

@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user
            course.save()
            return redirect('instructor_dashboard')
    else:
        form = CourseForm()
    return render(request, 'instructor/add_course.html', {'form': form})

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id, instructor=request.user)
    lectures = course.lectures.all().order_by('order')
    return render(request, 'instructor/course_detail.html', {'course': course, 'lectures': lectures})

@login_required
def add_lecture(request, course_id):
    course = get_object_or_404(Course, id=course_id, instructor=request.user)
    if request.method == 'POST':
        form = LectureForm(request.POST, request.FILES)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.course = course
            lecture.save()
            return redirect('course_detail', course_id=course.id)
    else:
        form = LectureForm()
    return render(request, 'instructor/add_lecture.html', {'form': form, 'course': course})

@login_required
def give_feedback(request, course_id):
    course = get_object_or_404(Course, id=course_id, instructor=request.user)
    students = [e.student for e in course.enrollments.all()]
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.instructor = request.user
            feedback.course = course
            feedback.save()
            return redirect('course_detail', course_id=course.id)
    else:
        form = FeedbackForm()
        form.fields['student'].queryset = course.enrollments.all().values_list('student', flat=True)
    return render(request, 'instructor/give_feedback.html', {'form': form, 'course': course})
