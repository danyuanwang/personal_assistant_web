from django.db import models

# Create your models here.
class ConversationLog(models.Model):
    from_user = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'conversation_log'

class FromAssistant(models.Model):
    recipient_id = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'from_assistant'

class FromUser(models.Model):
    sender = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'from_user'