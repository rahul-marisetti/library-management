from django.contrib import admin
from django.utils.timezone import now
from .models import Book, Member, Transaction

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'available')
    list_filter = ('available',)
    search_fields = ('title', 'author', 'isbn')

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'membership_date')
    search_fields = ('name', 'email')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'checkout_date', 'return_date', 'is_returned')
    list_filter = ('is_returned',)
    search_fields = ('book__title', 'member__name')

    def save_model(self, request, obj, form, change):
        # Check if the 'is_returned' field has been changed and is now True
        if obj.is_returned and 'is_returned' in form.changed_data:
            # Set the related Book's available status to True
            obj.book.available = True
            obj.book.save()
            # Set the return_date on the transaction
            obj.return_date = now()
        
        super().save_model(request, obj, form, change)
