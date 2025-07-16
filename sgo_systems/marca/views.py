from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Marca
from .forms import MarcaForm
from django.views import View

class MarcaList(View):
    template = "marca/listar_marcas.html"  # Adicione o diretório 'marca/'
    def get(self, request):
        return render(request, self.template, {"marcas": Marca.objects.all()})
    
class MarcaCreate(View):
    template = "marca/cadastrar_marca.html"  # Adicione o diretório 'marca/'
    def get(self, request):
        return render(request, self.template, {"form": MarcaForm()})
    
    def post(self, request):
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✔ Marca cadastrada com sucesso!")
            return redirect("marca:listar_marcas")  # Adicione o namespace
        return render(request, self.template, {"form": form})

class MarcaUpdate(View):
    template = "marca/editar_marca.html"  # Adicione o diretório 'marca/'
    def get(self, request, pk):
        marca = get_object_or_404(Marca, pk=pk)
        return render(request, self.template, {"form": MarcaForm(instance=marca)})
    
    def post(self, request, pk):
        marca = get_object_or_404(Marca, pk=pk)
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            messages.success(request, "✔ Marca editada com sucesso!")
            return redirect("marca:listar_marcas")  # Adicione o namespace
        return render(request, self.template, {"form": form})

class MarcaDelete(View):
    def post(self, request, pk):
        marca = get_object_or_404(Marca, pk=pk)
        marca.delete()
        messages.success(request, "Marca excluída com sucesso.")
        return redirect('marca:listar_marcas')  # Adicione o namespace
  
    def get(self, request, pk):
        marca = get_object_or_404(Marca, pk=pk)
        marca.delete()
        return redirect('marca:listar_marcas')  # Adicione o namespace
