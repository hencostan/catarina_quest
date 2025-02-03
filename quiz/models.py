from django.db import models

class Category(models.Model):
    """Modelo para armazenar as categorias de perguntas."""
    name = models.CharField(max_length=100, unique=True)  
    description = models.TextField(blank=True, null=True)  

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"  


class Question(models.Model):
    """Modelo para armazenar perguntas do quiz."""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="questions")  
    text = models.TextField()  
    correct_answer = models.CharField(max_length=200)  
    wrong_answer_1 = models.CharField(max_length=200)  
    wrong_answer_2 = models.CharField(max_length=200)  
    wrong_answer_3 = models.CharField(max_length=200)  
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.text} ({self.category.name})"

    class Meta:
        verbose_name_plural = "Questions" 