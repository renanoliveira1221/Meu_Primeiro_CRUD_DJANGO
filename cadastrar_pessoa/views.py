from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa

# Create your views here.


def cadastrar_pessoa(request):
    if request.method == "GET":
        pessoas = Pessoa.objects.all()
        return render(request, "index.html", {"pessoas": pessoas})
    elif request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        pessoa = Pessoa(nome=nome, email=email)
        pessoa.save()
        return redirect("cadastrar_pessoa")
    
    
def deletar_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    pessoa.delete()
    return redirect("cadastrar_pessoa")


def editar_pessoa(request, id):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    pessoa = get_object_or_404(Pessoa, id=id)
    pessoa.nome = nome
    pessoa.email = email
    pessoa.save()
    return redirect("cadastrar_pessoa")