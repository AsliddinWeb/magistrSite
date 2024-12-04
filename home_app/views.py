from django.http import JsonResponse
from django.shortcuts import render

from .models import (HomeWelcome, HomeWelcomeButton, CourseRightButton, Message,
                     AboutWelcome, AboutTeam, AboutAuthor, AboutResult, Quiz)
from news_app.models import News
from course_app.models import CourseCategory


def home(request):
    home_welcome = HomeWelcome.objects.last()
    home_welcome_buttons = HomeWelcomeButton.objects.all()

    news = News.objects.all()

    course_right_button = CourseRightButton.objects.last()
    course_categories = CourseCategory.objects.all()

    ctx = {
        'home_welcome': home_welcome,
        'home_welcome_buttons': home_welcome_buttons,

        'news': news,

        'course_right_button': course_right_button,
        'course_categories': course_categories,
    }

    return render(request, 'home.html', ctx)

def send_message(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if not all([name, phone, message]):
            return JsonResponse({'status': 'error', 'message': 'Barcha maydonlarni to\'ldiring!'}, status=400)

        Message.objects.create(
            name=name,
            phone=phone,
            message=message
        )

        return JsonResponse({'status': 'success', 'message': 'Xabar muvaffaqiyatli yuborildi!'})

    return JsonResponse({'status': 'error', 'message': 'Faqat POST so\'rovi qabul qilinadi!'}, status=405)


def about_page(request):
    about_welcome = AboutWelcome.objects.last()
    about_teams = AboutTeam.objects.all()
    about_results = AboutResult.objects.all()
    about_author = AboutAuthor.objects.last()

    ctx = {
        'about_welcome': about_welcome,
        'about_teams': about_teams,
        'about_results': about_results,
        'about_author': about_author,
    }

    return render(request, 'pages/about.html', ctx)

def quiz_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        quizes = Quiz.objects.all()

        if name:
            ctx = {
                'name': name,
                'quizes': quizes,
            }
            return render(request, "pages/questions.html", ctx)

        if "submit_answers" in request.POST:
            correct_count = 0
            total_questions = quizes.count()
            user_answers = {}

            for quiz in quizes:
                user_answer = request.POST.get(f"question_{quiz.id}")
                user_answers[quiz.id] = user_answer
                if user_answer and user_answer == quiz.correct_option:
                    correct_count += 1

            ctx = {
                'name': name,
                'total_questions': total_questions,
                'correct_count': correct_count,
                'user_answers': user_answers,
                'quizes': quizes,
            }

            return render(request, "pages/result.html", ctx)

    return render(request, 'pages/quiz.html')