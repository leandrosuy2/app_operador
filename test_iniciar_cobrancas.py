#!/usr/bin/env python
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from core.views import iniciar_cobrancas
from django.test import RequestFactory
from django.contrib.auth.models import User

print("Testando view iniciar_cobrancas...")

try:
    # Criar request factory
    rf = RequestFactory()
    
    # Obter primeiro usuário
    user = User.objects.first()
    if not user:
        print("ERRO: Nenhum usuário encontrado no banco de dados")
        sys.exit(1)
    
    # Criar request
    request = rf.get('/iniciar-cobrancas/')
    request.user = user
    
    # Testar view
    response = iniciar_cobrancas(request)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        print("✅ View funcionando corretamente!")
    else:
        print(f"❌ Erro na view: Status {response.status_code}")
        
except Exception as e:
    print(f"❌ Erro: {e}")
    import traceback
    traceback.print_exc()
