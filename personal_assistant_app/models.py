from django.db import models

# Create your models here.

class ActionLog(models.Model):
    request_json = models.TextField(blank=True, null=True)
    response_json = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'action_log'


class Actions(models.Model):
    action_id = models.TextField(primary_key=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actions'

class ConversationLog(models.Model):
    conversation_id = models.TextField(
        blank=True, null=True)
    from_user = models.TextField(blank=True, null=True)
    to_user = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'conversation_log'

class NlgLog(models.Model):
    conversation_id = models.TextField(blank=True, null=True)
    request_json = models.TextField(blank=True, null=True)
    response_json = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nlg_log'


class NlgTemplates(models.Model):
    template_id = models.TextField(primary_key=True)
    response_id = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    buttons = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    elements = models.TextField(blank=True, null=True)
    attachments = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nlg_templates'
