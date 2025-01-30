from django.contrib import admin
from .models import Category, Question  # Certifique-se de importar também o Question

# Registre os modelos no admin
admin.site.register(Category)
admin.site.register(Question)  # Adicionando o modelo Question ao admin