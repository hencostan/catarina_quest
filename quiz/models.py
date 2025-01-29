from django.db import models

class Category(models.Model):
    """Modelo para armazenar as categorias de perguntas."""
    name = models.CharField(max_length=100)  # Nome da categoria
    description = models.TextField()  # Descrição da categoria (opcional)

    def __str__(self):
        return self.name


class Question(models.Model):
    """Modelo para armazenar perguntas do quiz."""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Relaciona a categoria
    text = models.TextField()  # Texto da pergunta
    correct_answer = models.CharField(max_length=200)  # Resposta correta
    wrong_answer_1 = models.CharField(max_length=200)  # Primeira resposta errada
    wrong_answer_2 = models.CharField(max_length=200)  # Segunda resposta errada
    wrong_answer_3 = models.CharField(max_length=200)  # Terceira resposta errada

    def __str__(self):
        return self.text
