from django.contrib import admin
from .models import  Group, Event
# Register your models here.
@admin.register(Group)

class GroupAdmin(admin.ModelAdmin):
    field =  ( "name", "location", "description")
    list_display = ("id", "name", "location", "description")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
     field = ("team1", "team2", "time", "score1", "score2", "group")
     list_display = ("id", "team1", "team2", "time", "score1", "score2", "group")

