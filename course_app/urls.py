from django.urls import path

from .views import course_details

urlpatterns = [
    path('<int:category_id>/', course_details, name='course_details')
]
