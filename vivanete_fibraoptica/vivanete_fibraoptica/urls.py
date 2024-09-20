from django.contrib import admin
from django.urls import path, include
from django_distill import distill_path  # Certifique-se de que o distill_path está importado
from . import views

urlpatterns = [
    # URL personalizada do admin
    path('painel-adm/', admin.site.urls),

    # Sua página inicial com distill_path
    distill_path('', views.home, name='home', distill_func=lambda: None),

    # Inclui URLs do app contato com distill_path
    path('contato/', include('contato.urls')),

    # Outras rotas
    path('servicos/', include('servicos.urls')),
    path('sobre/', include('sobre.urls')),
]
