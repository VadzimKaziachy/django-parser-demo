from django.contrib import admin

from .models import HomeModel


class HomeAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(HomeModel, HomeAdmin)
