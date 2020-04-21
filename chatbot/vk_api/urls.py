from vk_api.views import handler
from django.urls import path

urlpatterns = [
        path('', handler, name='handler'),
]