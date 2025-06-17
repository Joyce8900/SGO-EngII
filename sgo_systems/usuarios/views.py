from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.utils.decorators import method_decorator

class Cadastro(View):
    def get(self, request):
        return render(request, 'cadastro.html')
    
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Já existe um usuário com esse username')
        user = User.objects.create_user(username= username, email=email, password=senha)
        user.save()
        return redirect('login')


class Login(View):
    def post(self, request):    
        username= request.POST.get('username')
        senha= request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        if user:
            login_django(request, user)
            return redirect('plataforma')
        else:
            return HttpResponse('usuario ou senha inválidos')
    
    def get(self, request):
        return render(request, 'login.html')
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Plataforma(View):
    def get(self, request):
        return HttpResponse('Plataforma')
