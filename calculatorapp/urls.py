from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.greetings),
    path('calculator',views.calculator,name='calculator')
]
