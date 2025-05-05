from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .forms import ModeloForm
from django.contrib import messages
from django.shortcuts import redirect
from .models import Modelo


def cadastrar_modelo(request):
  if request.method == "POST":
    form = ModeloForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "✔ Modelo cadastrado com sucesso!")
      return redirect(reverse('cadastrar_produto'))
  else:
    form = ModeloForm()
  return render(request, "cadastrar_modelo.html", {"form": form})

def listar_modelos(request):
    modelos = Modelo.objects.all().order_by('nome')  
    return render(request, "listar_modelos.html", {"modelos": modelos})

def editar_modelo(request, pk):
    modelo = Modelo.objects.get(pk=pk)
    if request.method == "POST":
        form = ModeloForm(request.POST, instance=modelo)
        if form.is_valid():
            form.save()
            return redirect("listar_modelos")
    else:
        form = ModeloForm(instance=modelo)

    return render(request, "editar_modelo.html", {"form": form})


def deletar_modelo (request, pk):
    modelo = Modelo.objects.get(pk=pk)
    modelo.delete() 
    return redirect("listar_modelos")
