# core/decorators.py
from functools import wraps
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect

def group_required(group_ids):
    """
    Restringe a view a usuários que pertençam a pelo menos um grupo em group_ids.
    Ex.: @group_required([3])  # grupo dos operadores
    """
    def decorator(view_func):
        @login_required
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            if request.user.is_superuser or request.user.groups.filter(id__in=group_ids).exists():
                return view_func(request, *args, **kwargs)
            messages.error(request, "Você não tem permissão para acessar esta página.")
            return redirect("lista_titulos")
        return _wrapped
    return decorator
