from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #выводит 1ое меню
    path('<str:menu1>/', views.menu0, name='menu0'), #выводит второй уровень
    path('<str:menu1>/<str:menu2>', views.menu1, name='menu1'), #третий уровень
    path('<str:menu1>/<str:menu2>/<str:menu3>', views.menu2, name='menu2'), #четвертый уровень
    path('<str:menu1>/<str:menu2>/<str:menu3>/<str:menu4>', views.menu3, name='menu3'), #пятый уровень
    path('<str:menu1>/<str:menu2>/<str:menu3>/<str:menu4>/<str:menu5>', views.menu4, name='menu4'),
   #path('porducts/food/semimanufactured/pelmeni/baron', views.menu#, name='menu#'),
]