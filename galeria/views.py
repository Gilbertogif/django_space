from django.shortcuts import render

def index(request):
    return render(request, 'galeria/index.html')

# Quando chegar uma nova requisição para está pagína,
# rebdirize esse arquivo. 

def imagem(request):
    return render(request, 'galeria/imagem.html')