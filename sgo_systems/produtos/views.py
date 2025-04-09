from django.shortcuts import render, request, redirect
from .models import Produtos
# Create your views here.
class cadastrar_produtos(request):
    if request.method == 'GET':
      render(request, "cadastrar_produtos.html")
    else:
      nome = request.POST.get("nome")
      preco = request.POST.get("preco")
      quantidade = request.POST.get("quantidade")
      cor = request.POST.get("cor")
      tamanho = request.POST.get("tamanho")
      marca = request.POST.get("marca")
      descricao = request.POST.get("descricao")

      produto = Produtos(nome=nome,preco=preco,quantidade=quantidade,cor=cor,tamanho=tamanho,marca=marca,descricao=descricao)
      produto.save()
      redirect ("listar_produtos")
      