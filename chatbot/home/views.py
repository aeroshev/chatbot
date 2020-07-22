from django.shortcuts import render


def home(request):
    context = {'message': 'Hello, Django World!'}
    return render(request, 'home/home.html', context)


def about(request):
    return render(request, 'home/about.html')


def create(request):
    return render(request, 'home/createTODO.html')
