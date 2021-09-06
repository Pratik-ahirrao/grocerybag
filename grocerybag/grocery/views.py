from django.shortcuts import render, redirect
from .forms import CreateUserForm
from .models import addItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required(login_url='login')
def index(req):
    item = addItem.objects.all()
    item_user = item.filter(user=req.user)
    return render(req, 'index.html', {'items': item_user})


@login_required(login_url='login')
def add(req):
    # item = addItem.objects.all()

    if req.method == 'POST':
        status = 'PENDING'
        if req.POST['Item status'] == '0':
            status = 'PENDING'
        elif req.POST['Item status'] == '1':
            status = 'BOUGHT'
        elif req.POST['Item status'] == '2':
            status = 'NOT AVAILABLE'
        new_item = addItem(
            name=req.POST['Item name'],
            quantity=req.POST['Item quantity'],
            status=status,
            date=req.POST['Date'],
            user=req.user
        )
        new_item.save()
        print(req.POST['Date'])
        return redirect('/')

    return render(req, "add.html")


@login_required(login_url='login')
def delete(req, pk):
    item = addItem.objects.get(id=pk)
    item.delete()
    return redirect('/')


@login_required(login_url='login')
def update(req, pk):
    item = addItem.objects.get(id=pk)
    if req.method == 'POST':
        status = 'PENDING'
        if req.POST['Item status'] == '0':
            status = 'PENDING'
        elif req.POST['Item status'] == '1':
            status = 'BOUGHT'
        elif req.POST['Item status'] == '2':
            status = 'NOT AVAILABLE'
        new_item = addItem.objects.get(id=pk)
        new_item.name = req.POST['Item name']
        new_item.quantity = req.POST['Item quantity']
        new_item.status = status
        new_item.date = req.POST['Date']
        new_item.save()
        return redirect('/')
    return render(req, "update.html", {'item': item})


def home(req):
    item = addItem.objects.all()
    return render(req, 'home.html', {'items': item})


def signUp(req):
    if req.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()

        if req.method == 'POST':
            form = CreateUserForm(req.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(req, 'Account created for ' + user)
                return redirect('login')
        context = {'form': form}
        return render(req, 'signup.html', context)


def loginPage(req):
    if req.user.is_authenticated:
        return redirect('/')
    else:
        if req.method == 'POST':
            username = req.POST.get('username')
            password = req.POST.get('password')

            user = authenticate(req, username=username, password=password)

            if user is not None:
                login(req, user)
                return redirect('/')
            else:
                messages.info(req, 'Username Or Password is incorrect!')
        context = {}
        return render(req, 'login.html', context)


def logoutUser(req):
    logout(req)
    return redirect('home')


def filterByDate(req):
    item = addItem.objects.all()
    return render(req, 'home.html', {'items': item})