from django.contrib import admin

from .models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'victory', 'draw', 'lose', 'goals_num', 'goals_conceded')