from django.http import HttpResponse


def home(request):
    message = 'Hello, Django!'
    return HttpResponse(message)
