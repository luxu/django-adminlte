from django.contrib import admin
from .models import City, Pecas, Itenspecas
from .forms import PecasForm, ItensPecasForm

class ItensPecasInline(admin.TabularInline):
    model = Itenspecas
    extra = 1


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    ...

@admin.register(Pecas)
class PecasAdmin(admin.ModelAdmin):
    form = PecasForm
    inlines = [ItensPecasInline]

