from django.conf.urls import url, include
from perfil.views import index

urlpatterns = [
    url(r'^$', index)
]