from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Quiz, Question, Choice, StudentAnswer,  QuizResult
from courses.models import Course

@login_required
def quiz_list(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    quizzes = course.quizzes.all()
    return render(request, "quizzes/quiz_list.html", {"course": course, "quizzes": quizzes})


@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)

    if request.method == "POST":
        score = 0
        total = quiz.questions.count()

        for question in quiz.questions.all():
            choice_id = request.POST.get(str(question.id))
            if choice_id:
                choice = Choice.objects.get(id=choice_id)
                StudentAnswer.objects.create(student=request.user, question=question, choice=choice)
                if choice.is_correct:
                    score += 1

        percentage = int((score / total) * 100) if total > 0 else 0
        QuizResult.objects.create(student=request.user, quiz=quiz, score=percentage)

        messages.success(request, f"Quiz submitted! Your score: {percentage}%")
        return redirect("quiz_result", quiz_id=quiz.id)

    return render(request, "quizzes/take_quiz.html", {"quiz": quiz})


@login_required
def quiz_result(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    result = QuizResult.objects.filter(student=request.user, quiz=quiz).last()
    return render(request, "quizzes/quiz_result.html", {"quiz": quiz, "result": result})
