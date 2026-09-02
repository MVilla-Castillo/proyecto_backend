from django.shortcuts import render


def index(request):
    return render(request, 'cowork/index.html')

def error_404(request):
    return render(request, 'templates/404.html')
