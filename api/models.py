from django.conf import settings
from django.db import models

class Score(models.Model):
    class Meta:
        db_table = 'score'
    
    point = models.IntegerField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    created_by = models.IntegerField(null=True)
    
    @property
    def username(self):
        return self.user.username