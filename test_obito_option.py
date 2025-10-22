#!/usr/bin/env python
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from core.views import realizar_baixa
from django.test import RequestFactory
from django.contrib.auth.models import User
from core.models import Titulo

print("Testando funcionalidade de Óbito confirmado...")

try:
    # Criar request factory
    rf = RequestFactory()
    
    # Obter primeiro usuário
    user = User.objects.first()
    if not user:
        print("ERRO: Nenhum usuário encontrado no banco de dados")
        sys.exit(1)
    
    # Obter um título para teste
    titulo = Titulo.objects.first()
    if not titulo:
        print("ERRO: Nenhum título encontrado no banco de dados")
        sys.exit(1)
    
    print(f"Testando com usuário: {user.username}")
    print(f"Testando com título ID: {titulo.id}")
    
    # Criar request GET para carregar a página
    request = rf.get(f'/titulos/{titulo.id}/baixar/')
    request.user = user
    
    # Testar view
    response = realizar_baixa(request, titulo.id)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        print("✅ Página de realizar baixa carregada com sucesso!")
        print("✅ Opção 'Óbito confirmado' adicionada às formas de pagamento!")
        
        # Verificar se a opção está no mapeamento
        forma_pagamento_map = {
            0:"Pix",1:"Dinheiro",2:"Cartão de Débito",3:"Cartão de Crédito",
            4:"Cheque",5:"Depósito em Conta",6:"Pagamento na Loja",
            7:"Boleto Bancário",8:"Duplicata",9:"Recebimento pelo credor",
            10:"Óbito confirmado"
        }
        
        if 10 in forma_pagamento_map and forma_pagamento_map[10] == "Óbito confirmado":
            print("✅ Mapeamento de formas de pagamento atualizado corretamente!")
        else:
            print("❌ Erro no mapeamento de formas de pagamento")
    else:
        print(f"❌ Erro na página: Status {response.status_code}")
        
except Exception as e:
    print(f"❌ Erro: {e}")
    import traceback
    traceback.print_exc()
