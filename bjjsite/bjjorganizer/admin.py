from django.contrib import admin

from .models import Competitor, Match, Tournament

# Register your models here.

admin.site.register(Tournament)
admin.site.register(Match)
admin.site.register(Competitor)
