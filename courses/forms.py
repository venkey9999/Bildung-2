from django import forms
from .models import Course, Lecture, Feedback

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'price']

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['title', 'content', 'video', 'file']

from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['student', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write feedback here...'}),
        }

    def __init__(self, *args, **kwargs):
        course = kwargs.pop('course', None)
        super().__init__(*args, **kwargs)
        if course:
            self.fields['student'].queryset = course.enrollments.values_list('student', flat=False)

