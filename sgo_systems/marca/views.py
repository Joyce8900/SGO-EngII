from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Marca
from .forms import MarcaForm


URL_MARCAS = 'marca:listar_marcas'

def cadastrar_marca(request):
    if request.method == "POST":
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✔ Marca cadastrada com sucesso!")
            return redirect(URL_MARCAS)
    else:
        form = MarcaForm()
    return render(request, "cadastrar_marca.html", {"form": form})

def listar_marcas(request):
    marcas = Marca.objects.all()
    return render(request, "listar_marcas.html", {"marcas": marcas})

def deletar_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if marca.produtos_set.exists():
        messages.error(request, "Não é possível excluir. Há produtos vinculados a esta marca.")
        return redirect(URL_MARCAS)
    marca.delete()
    messages.success(request, "Marca excluída com sucesso.")
    return redirect(URL_MARCAS)

def editar_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == "POST":
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            messages.success(request, "✔ Marca editada com sucesso!")
            return redirect(URL_MARCAS)
    else:
        form = MarcaForm(instance=marca)
    return render(request, "editar_marca.html", {"form": form})