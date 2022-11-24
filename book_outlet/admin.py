from django.contrib import admin
from .models import Book,Author,Address,Country

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug":("title",)}
    list_filter = ("title","rating",)
    list_display = ("title","author",)

# class BookInline(admin.TabularInline):
#     model = Book

# class CountryAdmin(admin.ModelAdmin):
#     inlines = [
#         BookInline,
#     ]

admin.site.register(Book,BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)

