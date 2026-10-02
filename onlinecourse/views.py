from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Submission


def course_details(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(
        request,
        "course_details_bootstrap.html",
        {"course": course}
    )


def submit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    questions = course.questions.all()

    score = 0
    total_marks = sum(q.marks for q in questions)

    if request.method == "POST":
        for question in questions:
            selected = request.POST.get(f"question_{question.id}")

            if selected:
                choice = question.choices.filter(
                    id=selected,
                    is_correct=True
                ).first()

                if choice:
                    score += question.marks

        submission = Submission.objects.create(
            course=course,
            student_name=request.POST.get("student_name", "Student"),
            score=score,
            total_marks=total_marks,
        )

        return redirect(
            "show_exam_result",
            submission_id=submission.id
        )

    return render(
        request,
        "exam.html",
        {
            "course": course,
            "questions": questions
        }
    )


def show_exam_result(request, submission_id):
    submission = get_object_or_404(
        Submission,
        id=submission_id
    )

    return render(
        request,
        "exam_result.html",
        {"submission": submission}
    )