from rest_framework import serializers
from .models import Category, Question

class CategorySerializer(serializers.ModelSerializer):
    """Serializer para o modelo Category."""
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class QuestionSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Question."""
    class Meta:
        model = Question
        fields = [
            'id',
            'category',
            'text',
            'correct_answer',
            'wrong_answer_1',
            'wrong_answer_2',
            'wrong_answer_3',
        ]