from django.contrib import admin
from django.urls import path, include
from onlinecourse import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("onlinecourse.urls")),

    path(
        "course/<int:course_id>/exam/",
        views.submit,
        name="submit"
    ),

    path(
        "exam/result/<int:submission_id>/",
        views.show_exam_result,
        name="show_exam_result"
    ),
]