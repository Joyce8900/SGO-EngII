from django.shortcuts import redirect, render
from .models import Marca
from .forms import MarcaForm
from django.contrib import messages
# Create your views here.

def cadastrar_marca(request):
  if request.method == "POST":
    form = MarcaForm(request.POST)
    if form.is_valid():
      form.save()
      marca = Marca()
      messages.success(request, "✔ Marca cadastrada com sucesso!")
      return redirect("listar_marcas")
  else:
    form = MarcaForm()
  return render(request, "cadastrar_marca.html", {"form": form})

def listar_marcas(request):
  marcas = Marca.objects.all()
  return render(request, "listar_marcas.html", {"marcas": marcas})