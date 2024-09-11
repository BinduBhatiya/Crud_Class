from django.contrib import admin
from .models import Student

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("first_nm","last_nm","mail","city",)

admin.site.register(Student, MemberAdmin)