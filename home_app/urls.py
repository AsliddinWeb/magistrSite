from django.urls import path

from .views import home, send_message, about_page, quiz_page

urlpatterns = [
    # Home
    path('', home, name='home_page'),

    # Send message
    path('send-message/', send_message, name='send_message'),

    # About
    path('about/', about_page, name='about_page'),

    # Quiz
    path('quiz/', quiz_page, name='quiz_page'),
]
