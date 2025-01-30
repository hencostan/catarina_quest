import random
from rest_framework import serializers
from .models import Category, Question

class CategorySerializer(serializers.ModelSerializer):
    """Serializer para o modelo Category."""
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class QuestionSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Question."""
    options = serializers.SerializerMethodField()
    correctOption = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = [
            'id',
            'category',
            'text',
            'options',
            'correctOption'
        ]

    def get_options(self, obj):
        """Cria uma lista com as opções e as embaralha"""
        options = [
            {"text": obj.correct_answer, "is_correct": True},
            {"text": obj.wrong_answer_1, "is_correct": False},
            {"text": obj.wrong_answer_2, "is_correct": False},
            {"text": obj.wrong_answer_3, "is_correct": False},
        ]
        random.shuffle(options)  # Embaralha a lista
        return [opt["text"] for opt in options]

    def get_correctOption(self, obj):
        """Retorna o novo índice da resposta correta após o embaralhamento"""
        options = [
            {"text": obj.correct_answer, "is_correct": True},
            {"text": obj.wrong_answer_1, "is_correct": False},
            {"text": obj.wrong_answer_2, "is_correct": False},
            {"text": obj.wrong_answer_3, "is_correct": False},
        ]
        random.shuffle(options)  # Embaralha novamente
        return next(index for index, opt in enumerate(options) if opt["is_correct"])