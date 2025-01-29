from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "endpoints": {
            "questions": "/api/questions/",
            "categories": "/api/categories/"
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('quiz.urls')),  # Essa linha precisa estar antes do `api_root`
    path('', api_root),  # Agora a rota principal retorna os endpoints sem sobrescrever `api/`
]