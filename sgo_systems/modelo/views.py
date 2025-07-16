from django.shortcuts import render
from django.views import View
from .forms import ModeloForm
from django.contrib import messages
from django.shortcuts import redirect
from .models import Modelo
from django.shortcuts import get_object_or_404
URL_LISTAR_MODELOS = ("listar_modelos.html")
URL_EDITAR_MODELO = ("editar_modelo.html")
URL_CADASTRAR_MODELO = ("cadastrar_modelo.html")
URL_MODELOS = 'modelo:listar_modelos'


class CadastrarModelo(View):
  def get(self, request):
    form = ModeloForm()
    return render(request, URL_CADASTRAR_MODELO, {"form": form})
     
  def post(self, request):
    form = ModeloForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "✔ Modelo cadastrado com sucesso!")
      return redirect(URL_MODELOS)
    return render(request, URL_CADASTRAR_MODELO, {"form": form} )
     

class ListarModelos(View):
  def get(self, request):
    modelos = Modelo.objects.all().order_by('nome')
    return render(request, URL_LISTAR_MODELOS, {"modelos": modelos})


class EditarModelo(View):
  def get(self, request, pk):
    modelo = get_object_or_404(Modelo, pk=pk)
    form = ModeloForm(instance=modelo)
    return render(request, URL_EDITAR_MODELO, {"form": form})
  
  def post(self, request, pk):
    modelo = get_object_or_404(Modelo, pk=pk)
    form = ModeloForm(request.POST, instance=modelo)
    if form.is_valid():
      form.save()
      messages.success(request, "✔ Modelo editado com sucesso!")
      return redirect(URL_MODELOS)
    return render(request, URL_EDITAR_MODELO, {"form": form})



class DeletarModelo(View):
  def post(self, request, pk):
    modelo = get_object_or_404(Modelo, pk=pk)
    modelo.delete()
    messages.success(request, "Modelo excluído com sucesso.")
    return redirect(URL_MODELOS)
  
  def get(self, request, pk):
    modelo = get_object_or_404(Modelo, pk=pk)
    modelo.delete()
    return redirect(URL_MODELOS)

  


