from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib import messages


class Cadastro(View):
    def get(self, request):
        return render(request, 'cadastro.html')
    
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=username).first()
        if user:
            messages.error(request, 'Já existe um usuário com esse username.')
            return render(request, 'cadastro.html')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
        return redirect('login')


class Login(View):
    def post(self, request):    
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        if user:
            login_django(request, user)
            return redirect('home/')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'login.html', {
                'username': username  # Mantém o username digitado
            })
    
    def get(self, request):
        return render(request, 'login.html')


@method_decorator(login_required(login_url='login'), name='dispatch')
class Home(View):
    def get(self, request):
        return render(request, 'home/home.html')
