from django.contrib import admin

# Register your models here.

from django.contrib.auth import admin as auth_admin
from .forms import UserChangeForm, UserCreationForm

# Register your models here.

from .models import User, Agendamento, Hotel

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        (None, {'fields': ('endereco',)}),
        (None, {'fields': ('rg',)}),
        (None, {'fields': ('cpf',)}),
        (None, {'fields': ('telefone',)}),
    )

admin.site.register(Agendamento)
admin.site.register(Hotel)
