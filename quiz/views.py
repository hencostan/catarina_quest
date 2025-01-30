from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Question, Category
from .serializers import QuestionSerializer, CategorySerializer
import random

class CategoryList(ListAPIView):
    """View para listar todas as categorias disponíveis."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionList(APIView):
    """View para listar perguntas filtradas por categoria, embaralhando as respostas."""

    def get(self, request):
        category_id = request.query_params.get('category', None)
        
        if not category_id:
            return Response({"error": "É necessário fornecer um ID de categoria."}, status=400)

        category = get_object_or_404(Category, id=category_id)
        questions = Question.objects.filter(category=category)
        
        if not questions.exists():
            return Response({"message": "Nenhuma pergunta encontrada para essa categoria."}, status=404)

        # Serializando perguntas e embaralhando as opções de resposta
        serialized_questions = []
        for question in questions:
            options = [
                question.correct_answer,
                question.wrong_answer_1,
                question.wrong_answer_2,
                question.wrong_answer_3
            ]
            random.shuffle(options)  # Embaralha as opções

            serialized_questions.append({
                "id": question.id,
                "category": question.category.id,
                "question": question.text,
                "options": options,
                "correct_option": options.index(question.correct_answer),  # Guarda o índice correto
            })

        return Response(serialized_questions, status=200)