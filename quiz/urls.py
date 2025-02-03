from django.urls import path
from .views import CategoryList, QuestionList

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('questions/', QuestionList.as_view(), name='question-list'),
]