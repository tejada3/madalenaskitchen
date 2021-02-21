from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def menu(request):
    hot = MenuItem.objects.filter(type='Hot Sandwhiches').filter(available=True)
    cold = MenuItem.objects.filter(type='Cold Sandwhiches').filter(available=True)
    entress = MenuItem.objects.filter(type='Entress').filter(available=True)
    burgers = FoodsofTheWeek.objects.filter(type='Burger').filter(available=True)
    dessert = FoodsofTheWeek.objects.filter(type='Dessert').filter(available=True)

    return render(request, 'menupages/menu.html', {'hot': hot,
                                                   'cold': cold,
                                                   'entress': entress,
                                                   'burger': burgers,
                                              'dessert': dessert})

@login_required(login_url='login')
def menucontrol(request):
    hot = MenuItem.objects.filter(type='Hot Sandwhiches')
    cold = MenuItem.objects.filter(type='Cold Sandwhiches')
    entress = MenuItem.objects.filter(type='Entress')
    burgers = FoodsofTheWeek.objects.filter(type='Burger')
    dessert = FoodsofTheWeek.objects.filter(type='Dessert')

    return render(request, 'menupages/MenuControl.html', {'hot': hot,
                                                   'cold': cold,
                                                   'entress': entress,
                                                   'burger': burgers,
                                              'dessert': dessert})
@login_required(login_url='login')
def menuchangeavailablity(request, pk):
    item = MenuItem.objects.get(id=pk)
    if not item.available:
        i = MenuItem.objects.filter(id=pk).update(available=True)
    elif item.available:
        i = MenuItem.objects.filter(id=pk).update(available=False)
    else:
        print(item)
        return redirect('/menu-controls/')

    return redirect('/menu-controls/#')

@login_required(login_url='login')
def changeavailability(request, pk):
    item = FoodsofTheWeek.objects.get(id=pk)
    if not item.available:
        i = FoodsofTheWeek.objects.filter(id=pk).update(available=True)
    elif item.available:
        i = FoodsofTheWeek.objects.filter(id=pk).update(available=False)
    else:
        print(item)
        return redirect('/menu-controls/')

    return redirect('/menu-controls/')


@login_required(login_url='login')
def editMenu(request, pk):
    try:
        item = MenuItem.objects.get(id=pk)
        iform = MenuItemForm(instance=item)
        if request.method == "POST":
            iform = MenuItemForm(request.POST, request.FILES, instance=item)
            if iform.is_valid():
                iform.save()

                return redirect('/menu-controls/')
            else:
                print('in here')
            print("done")

    except:
        item = FoodsofTheWeek.objects.get(id=pk)
        iform = FoodsOfTheWeekForm(instance=item)
        if request.method == "POST":
            iform = FoodsOfTheWeekForm(request.POST, request.FILES, instance=item)
            if iform.is_valid():
                iform.save()

                return redirect('/menu-controls/')

            else:
                print('in here')
        print("done")
    return render(request, 'menupages/item-update.html', {'item': iform})


@login_required(login_url='login')
def addToMenu(request):
    iform = MenuItemForm()
    if request.method == "POST":
        iform = MenuItemForm(request.POST, request.FILES)
        if iform.is_valid():

            iform.save()
            return redirect('/menu-controls/')
        else:
            print('in here')

        print("done")
    return render(request, 'menupages/item-add.html', {'item': iform})


@login_required(login_url='login')
def addFOTW(request):
    iform = FoodsOfTheWeekForm()
    if request.method == "POST":
        iform = FoodsOfTheWeekForm(request.POST, request.FILES)
        if iform.is_valid():
            iform.save()
            return redirect('/menu-controls/')
        else:
            print('in here')
    return render(request, 'menupages/add-FOTW.html', {'item': iform})


@login_required(login_url='login')
def deleteitem(request, pk):
    dele = MenuItem.objects.filter(id=pk)
    print(dele)
    dele.delete()
    return redirect('/menu-controls/')


@login_required(login_url='login')
def deleteFOTW(request, pk):
    dele = FoodsofTheWeek.objects.filter(id=pk)
    print(dele)
    dele.delete()
    return redirect('/menu-controls/')


def Login(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(user)

                return redirect('menu-controls')
            else:
                messages.info(request, 'USERNAME or PASSWAORD is incorrect')
                context = {'messege': "WORNG USERNAME OR PASSWORD"}
                return render(request, 'menupages/login.html', context)

        return render(request, 'menupages/login.html',)