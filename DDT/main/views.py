import decimal

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Balance, Lender, Borrower
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView


def home(request):
    return render(request, 'home.html',)


def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid username and password"}
            return render(request, "login.html", context)
        login(request, user)
        return redirect('/profile/')
    return render(request, 'login.html', )


class borrowers(ListView):
    model = Borrower
    template_name = 'borrowers.html'
    ordering = '-date_created'

    def get_queryset(self):
        return Borrower.objects.filter(Lender_approval=False).order_by('-date_created')


class LenderList(ListView):
    model = Lender
    template_name = 'lender.html'
    ordering = '-date_created'

    def get_queryset(self):
        return Lender.objects.filter(Borrower_approval=False).order_by('-date_created')


#View to make Pledge loan
@login_required
def CreateLender(request):
    try:
        balance = request.user.balance
    except Balance.DoesNotExist:
        balance = None
    if request.method == 'POST':
        lender = Balance.objects.get(user=request.user)
        user = request.user
        amount = request.POST.get('amount')
        conditions = request.POST.get('conditions')
        percentage = request.POST.get('percentage')
        duration = request.POST.get('duration')
        if lender.balance < decimal.Decimal(request.POST.get('amount')):
            transaction = 'Sorry! You do not have enough fund to pledge'
            return render(request, 'create_lender.html', {'transaction': transaction})
        else:
            borrow = Lender.objects.create(user=request.user, amount=amount, conditions=conditions, percentage=percentage, duration=duration)
            borrow.save()
            return redirect('/lenders/')
    return render(request,'create_lender.html', {'balance':balance})

#View to Request for loan
@login_required
def CreateBorrower(request):
    try:
        balance = request.user.balance
    except Balance.DoesNotExist:
        balance = None
    if request.method == 'POST':
        user = request.user
        amount = request.POST.get('amount')
        conditions = request.POST.get('conditions')
        percentage = request.POST.get('percentage')
        duration = request.POST.get('duration')
        borrowing = Borrower.objects.create(user=request.user, amount=amount, conditions=conditions, percentage=percentage, duration=duration)
        borrowing.save()
        return redirect('/borrowers/')
    return render(request, 'create_borrower.html', {'balance': balance})

def Logout(request):
    logout(request)
    return redirect('/login/')


def Register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        msg = {'Msg': 'Account created successfully'}
        return redirect('login/')

    context = {
        "form":form,
    }
    return render(request, 'register.html',context)


@login_required
def profile(request):
    try:
        balance = request.user.balance
    except Balance.DoesNotExist:
        balance = None
    return render(request, 'profile.html', {'balance': balance})

@login_required()
def lenderDetails(request, id):
    try:
        balance = request.user.balance
    except Balance.DoesNotExist:
        balance = None
    lender = get_object_or_404(Lender, id=id)
        
    return render(request, 'lender_details.html', {'lender':lender, 'balance': balance})


@login_required()
def borrowers_details(request, id):
    try:
        balance = request.user.balance
    except Balance.DoesNotExist:
        balance = None
    borrower = get_object_or_404(Borrower, id=id)
    return render(request, 'borrowers_details.html', {'borrowers':borrower, 'balance': balance})

