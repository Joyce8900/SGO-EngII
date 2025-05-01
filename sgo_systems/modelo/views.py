from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .forms import ModeloForm
from django.contrib import messages
from django.shortcuts import redirect

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