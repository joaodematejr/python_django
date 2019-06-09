from django.contrib import admin
from django.urls import path, include
from simplemooc.core import views  # regra devida versão 2.0 do Django
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('contato/', views.contact, name='contact'),
]
