from django.shortcuts import render

from .models import HomeWelcome, HomeWelcomeButton, CourseRightButton
from news_app.models import News


def home(request):
    home_welcome = HomeWelcome.objects.last()
    home_welcome_buttons = HomeWelcomeButton.objects.all()

    news = News.objects.all()

    course_right_button = CourseRightButton.objects.last()

    ctx = {
        'home_welcome': home_welcome,
        'home_welcome_buttons': home_welcome_buttons,

        'news': news,

        'course_right_button': course_right_button,
    }

    return render(request, 'home.html', ctx)
