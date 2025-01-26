from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .forms import ArtigoForm
from .models import Artigo


# Create your views here.

def home(request):
    artigos = Artigo.objects.all()
    return render(request,'home.html', {'artigos': artigos})


def artigo(request):
    artigos = Artigo.objects.all()
    return render(request,'artigo.html', {'artigos': artigos})

@login_required(login_url="/login/")
def configuracoes(request):
    artigos = Artigo.objects.all()  
    return render(request, 'configuracoes.html', {'artigos': artigos})

@login_required(login_url="/login/")
def adicionar(request):
    if request.method == "POST":
        form = ArtigoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adicionar')
    else:
        form = ArtigoForm()
    
    return render(request,'adicionar.html', {'form':form})

@login_required(login_url="/login/")
def editar(request, artigo_id):
    # Obtém o artigo pelo ID; se não for encontrado, retorna um erro 404
    artigo = get_object_or_404(Artigo, id=artigo_id)

    if request.method == "POST":
        # Cria o formulário com os dados enviados na requisição e vincula ao artigo existente
        form = ArtigoForm(request.POST, instance=artigo)
        if form.is_valid():
            form.save()  # Salva as alterações no banco de dados
            return redirect('configuracoes')  # Redireciona para a página de configurações
    else:
        # Cria o formulário com os dados do artigo existente para edição
        form = ArtigoForm(instance=artigo)

    # Renderiza a página de edição com o formulário e o artigo
    return render(request, 'editar.html', {'form': form, 'artigo': artigo})



def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha )
        if user:
            login_django(request, user)
            return render(request, 'configuracoes.html')
        else:
            return HttpResponse("Email ou senha invalidos")




        

