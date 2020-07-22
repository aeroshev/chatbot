from django.urls import path
from home.views import home, about, create


urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about, name='about'),
    path('create/', create, name='create')
]