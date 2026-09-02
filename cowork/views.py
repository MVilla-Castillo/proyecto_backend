from django.shortcuts import render


def index(request):
    return render(request, 'cowork/index.html')
