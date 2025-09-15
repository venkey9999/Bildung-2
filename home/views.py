from django.shortcuts import render
from courses.models import Course

def guest_home(request):
    courses = Course.objects.all()[:6]  # show first 6
    return render(request, "home/guest_home.html", {"courses": courses})
