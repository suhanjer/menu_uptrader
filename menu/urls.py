from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:menu1>/', views.menu4, name='menu0'),
    path('<str:menu1>/<str:menu2>', views.menu1, name='menu1'),
    path('<str:menu1>/<str:menu2>/<str:menu3>', views.menu2, name='menu2'),
    path('<str:menu1>/<str:menu2>/<str:menu3>/<str:menu4>', views.menu3, name='menu3'),
    path('<str:menu1>/<str:menu2>/<str:menu3>/<str:menu4>/<str:menu5>', views.menu4, name='menu4'),
]