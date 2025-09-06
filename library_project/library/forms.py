from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Transaction,Book,Member

class SignUpForm(UserCreationForm):
    email=forms.EmailField(required=True,max_length=200,help_text="example:example@gmail.com")
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
class BorrowForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('book',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the books queryset to only show available books
        self.fields['book'].queryset = Book.objects.filter(available=True)

