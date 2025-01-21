from django.urls import path
from .views import CategoryList, QuestionList

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='categories'),
    path('questions/', QuestionList.as_view(), name='questions'),
]