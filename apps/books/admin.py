from django.contrib import admin
from .models import Books

class BooksAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'publisher', 'sale_price', 'price_on_book', 'isnew', 'created_at', 'last_modified']

    def isnew(self, obj):
        if obj.is_new:
            return True
        return False
    
    # Show tick/cross icon in admin page
    isnew.boolean = True


admin.site.register(Books, BooksAdmin)