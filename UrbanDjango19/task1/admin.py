from django.contrib import admin
from .models import Game, Buyer

# Register your models here.

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')
    list_filter = ('size', 'cost')
    list_max_show_all = 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age')
    list_display = ('username', 'balance', 'age')
    search_fields = ('name',)
    readonly_fields = ('balance',)
    list_max_show_all = 30

    fieldsets = ((None, {
        'fields': ('username', 'balance', 'age')
    }),)