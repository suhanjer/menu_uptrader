from django.shortcuts import render
from .models import Menu0, Menu1, Menu2, Menu3, Menu4

code = 0

# Create your views here.
def index(request):
    return render(request, "menu/index.html", {
        'menus': Menu0.objects.all(),
    })

def menu0(request, menu1):
    selected1 = Menu0.objects.get(code=menu1)
    return render(request, "menu/index.html", {
        'menus': Menu0.objects.all(),
        'menus1': selected1.level1.all(),
        'code': menu1,
    })

def menu1(request, menu1, menu2):
    selected1 = Menu0.objects.get(code=menu1)
    selected2 = Menu1.objects.get(code=menu2)
    print(Menu0.objects.all())
    print(selected1.level1.all())
    return render(request, "menu/index.html", {
        'menus': Menu0.objects.all(),
        'menus1': selected1.level1.all(),
        'menus2': selected2.level2.all(),
        'code': menu2,
    })

def menu2(request, menu1, menu2, menu3):
    selected1 = Menu0.objects.get(code=menu1)
    selected2 = Menu1.objects.get(code=menu2)
    selected3 = Menu2.objects.get(code=menu3)
    return render(request, "menu/index.html", {
        'menus': Menu0.objects.all(),
        'menus1': selected1.level1.all(),
        'menus2': selected2.level2.all(),
        'menus3': selected3.level3.all(),
        'code': menu3,
    })

def menu3(request, menu1, menu2, menu3, menu4):
    selected1 = Menu0.objects.get(code=menu1)
    selected2 = Menu1.objects.get(code=menu2)
    selected3 = Menu2.objects.get(code=menu3)
    selected4 = Menu3.objects.get(code=menu4)
    return render(request, "menu/index.html", {
        'menus': Menu0.objects.all(),
        'menus1': selected1.level1.all(),
        'menus2': selected2.level2.all(),
        'menus3': selected3.level3.all(),
        'menus4': selected4.level4.all(),
        'code': menu4,
    })

def menu4(request, menu1, menu2, menu3, menu4, menu5):
    selected1 = Menu0.objects.get(code=menu1)
    selected2 = Menu1.objects.get(code=menu2)
    selected3 = Menu2.objects.get(code=menu3)
    selected4 = Menu3.objects.get(code=menu4)
    return render(request, "menu/index.html", {
        'menus': Menu0.objects.all(),
        'menus1': selected1.level1.all(),
        'menus2': selected2.level2.all(),
        'menus3': selected3.level3.all(),
        'menus4': selected4.level4.all(),
        'code': menu5,
    })