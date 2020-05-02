from django.db import models

# Create your models here.
class ConversationLog(models.Model):
    from_user = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'conversation_log'
