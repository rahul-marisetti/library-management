from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, BorrowForm
from django.contrib.auth.decorators import login_required
from .models import Book, Member, Transaction
from django.utils.timezone import now
from django.contrib import messages

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            member = Member.objects.create(name=user.username, email=user.email)
            login(request, user)
            return redirect("main")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("main")
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

@login_required
def main_view(request):
    # Fetch the actual lists of books and transactions
    available_books_list = Book.objects.filter(available=True)
    borrowed_transactions_list = Transaction.objects.filter(is_returned=False)
    
    context = {
        'user': request.user,
        'total_books': Book.objects.count(),
        'available_books': available_books_list.count(),
        'total_members': Member.objects.count(),
        'borrowed_books': borrowed_transactions_list.count(),
        'overdue_books': Transaction.objects.filter(is_returned=False, return_date__lt=now()).count(),
        'available_books_list': available_books_list,
        'borrowed_transactions_list': borrowed_transactions_list
    }
    return render(request, 'main.html', context)

@login_required
def account_details_view(request):
    # Check if a Member object exists, if not, create one
    try:
        member = Member.objects.get(email=request.user.email)
    except Member.DoesNotExist:
        member = Member.objects.create(name=request.user.username, email=request.user.email)

    borrowed_books_count = Transaction.objects.filter(member=member, is_returned=False).count()
    returned_books_count = Transaction.objects.filter(member=member, is_returned=True).count()

    context = {
        'member': member,
        'borrowed_books_count': borrowed_books_count,
        'returned_books_count': returned_books_count,
    }
    return render(request, 'account_details.html', context)

@login_required
def transactions_history_view(request):
    # Check if a Member object exists, if not, create one
    try:
        member = Member.objects.get(email=request.user.email)
    except Member.DoesNotExist:
        member = Member.objects.create(name=request.user.username, email=request.user.email)

    transactions = Transaction.objects.filter(member=member).order_by('-checkout_date')
    context = {'transactions': transactions}
    return render(request, 'transactions_history.html', context)

@login_required
def make_transaction_view(request):
    # Get available books for the search bar and the form
    search_query = request.GET.get('q', '')
    available_books = Book.objects.filter(available=True, title__icontains=search_query)

    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']
            # Check if a Member object exists, if not, create one
            try:
                member = Member.objects.get(email=request.user.email)
            except Member.DoesNotExist:
                member = Member.objects.create(name=request.user.username, email=request.user.email)

            # Create the transaction
            Transaction.objects.create(member=member, book=book)

            # Update the book's availability
            book.available = False
            book.save()

            messages.success(request, f'Successfully borrowed "{book.title}"!')

            return redirect('transactions_history')
    else:
        form = BorrowForm()

    context = {
        'form': form,
        'available_books': available_books,
        'search_query': search_query
    }
    return render(request, 'make_transaction.html', context)

def logout_view(request):
    logout(request)
    return redirect("login")