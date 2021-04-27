from django.urls import path
from .views import home, env

urlpatterns = [
    path('', home, name='home'),
    path('env', env, name='env')

]
