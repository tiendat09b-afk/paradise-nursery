from django.shortcuts import render
from .models import Question, Choice, Submission


def submit(request):

    if request.method == "POST":
        question_id = request.POST.get("question")
        choice_id = request.POST.get("choice")

        question = Question.objects.get(id=question_id)
        choice = Choice.objects.get(id=choice_id)

        Submission.objects.create(
            question=question,
            choice=choice
        )

    return render(request, "submit.html")


def show_exam_result(request):

    submissions = Submission.objects.all()

    context = {
        "submissions": submissions
    }

    return render(request, "result.html", context)
