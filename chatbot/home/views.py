from django.shortcuts import render


def home(request):
    context = {'message': 'Hello, Django World!'}
    return render(request, 'index.html', context)
