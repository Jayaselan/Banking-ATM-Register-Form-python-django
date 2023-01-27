  from django.shortcuts import render
from django.http import HttpResponse
from .models import user1
from .models import created1
# from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


def create(request):
    return render(request, 'create.html')


def created(request):
    #  UserName=None
    #  Password=None
    if request.method == "POST":
        UserName = request.POST['UserName']
        Password = request.POST['Password']
        Fname = request.POST['Fname']
        Lname = request.POST['Lname']
        Email = request.POST['Email']
        Pass1 = request.POST['Pass1']
        Mobile = request.POST['Mobile']
        Branch = request.POST['Branch']
        obj = created1()
        obj.Username = UserName
        obj.password1 = Password
        obj.Fname = Fname
        obj.Lname = Lname
        obj.pass1 = Pass1
        obj.mobile = Mobile
        obj.branch = Branch
        obj.save()
    return render(request, 'created.html', {'username': UserName, 'password': Password, 'fname': Fname, 'lname': Lname, 'email': Email, 'pass1': Pass1, 'mobile': Mobile, 'branch': Branch})


def atm(request):
    UserName = None
    Password = None
    if request.method == "POST":
        UserName = request.POST['UserName']
        Password = request.POST['Password']
        obj = user1()
        obj.Name = UserName
        obj.password = Password
        obj.save()
    return render(request, 'atm.html', {'username': UserName, 'password': Password})


def saving(request):
    return render(request, 'saving.html')


def wm(request):
    return render(request, 'withdrawal.html')


def get_money(request):
    Amount = None
    if request.method == 'POST':
        Amount = request.POST['Amount']
    return render(request, 'amt.html', {'amt': Amount})


def mini_statement(request):
    return render(request, 'mini_statement.html')


def balance(request):
    return render(request, 'balance.html')


def card(request):

    return render(request, 'card_block.html')


def enq(request):
    return render(request, 'enquire.html')


def contact(request):
    return render(request, 'contact_us.html')


def track(request):
    return render(request, 'track_atm.html')


def about(request):
    return render(request, 'About_us.html')
