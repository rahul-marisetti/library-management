from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 Character ISBN number')
    publication_date=models.DateTimeField(auto_now_add=True)
    available=models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    
class Member(models.Model):
    name=models.CharField(max_length=75)
    email=models.EmailField(unique=True)
    membership_date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class Transaction(models.Model):
    member=models.ForeignKey(Member, on_delete=models.CASCADE)
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout_date=models.DateField(auto_now_add=True)
    return_date=models.DateField(null=True, blank=True)
    is_returned=models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.member.name} checked out {self.book.title}"
    