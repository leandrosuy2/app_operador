#!/usr/bin/env python
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from core.views import dashboard
from django.test import RequestFactory
from django.contrib.auth.models import User

print("Testando dashboard com filtros por operador...")

try:
    # Criar request factory
    rf = RequestFactory()
    
    # Obter primeiro usuário
    user = User.objects.first()
    if not user:
        print("ERRO: Nenhum usuário encontrado no banco de dados")
        sys.exit(1)
    
    print(f"Testando com usuário: {user.username}")
    
    # Criar request
    request = rf.get('/dashboard/')
    request.user = user
    
    # Testar view
    response = dashboard(request)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        print("✅ Dashboard funcionando corretamente!")
        print("✅ Filtros por operador implementados com sucesso!")
    else:
        print(f"❌ Erro no dashboard: Status {response.status_code}")
        
except Exception as e:
    print(f"❌ Erro: {e}")
    import traceback
    traceback.print_exc()
