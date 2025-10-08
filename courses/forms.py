from django import forms
from django.utils.text import slugify
from .models import Course, Lecture, Feedback, Enrollment


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'slug', 'description', 'price', 'cover_image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4})
        }

    def clean_slug(self):
        slug = self.cleaned_data.get('slug') or slugify(self.cleaned_data.get('title', ''))
        if Course.objects.filter(slug=slug).exists():
            raise forms.ValidationError("This slug is already taken. Try another one.")
        return slug


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['title', 'content', 'video', 'file']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write feedback here...'}),
        }

    def __init__(self, *args, **kwargs):
        course = kwargs.pop('course', None)  # passed from view
        super().__init__(*args, **kwargs)
        if course:
            # restrict feedback to enrolled students
            enrolled_students = Enrollment.objects.filter(course=course).values_list("student", flat=True)
            self.fields['student'].queryset = course.students.filter(id__in=enrolled_students)
