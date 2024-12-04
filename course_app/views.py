from django.shortcuts import render, get_object_or_404

from .models import Course, CourseCategory

def course_details(request, category_id):
    category = get_object_or_404(CourseCategory, id=category_id)

    courses = Course.objects.filter(category=category)

    ctx = {
        'category': category,
        'courses': courses
    }

    return render(request, 'pages/course_details.html', ctx)
