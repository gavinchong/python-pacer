from django.contrib import admin
from .models import Score

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'point', 'username', 'created_at')
    search_fields = ('user_id__username', 'point')
    list_editable = ('point',)

# Register your models here.
admin.site.register(Score, ScoreAdmin)