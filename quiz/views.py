from django.shortcuts import render

from rest_framework.generics import ListAPIView
from .models import Question, Category
from .serializers import QuestionSerializer, CategorySerializer

class CategoryList(ListAPIView):
    """View para listar todas as categorias."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionList(ListAPIView):
    """View para listar perguntas filtradas por categoria."""
    serializer_class = QuestionSerializer

    def get_queryset(self):
        """Filtra perguntas com base no parâmetro de categoria."""
        category_name = self.request.query_params.get('category', None)
        if category_name:
            return Question.objects.filter(category__name__iexact=category_name)
        return Question.objects.all()