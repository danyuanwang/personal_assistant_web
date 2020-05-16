from django.db import models

# Create your models here.


class ConversationLog(models.Model):
    conversation_id = models.TextField(
        blank=True, null=True)
    from_user = models.TextField(blank=True, null=True)
    to_user = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'conversation_log'
