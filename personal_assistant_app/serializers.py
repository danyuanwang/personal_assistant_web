from personal_assistant_app.models import Actions
from personal_assistant_app.models import ActionLog
from personal_assistant_app.models import ConversationLog
from personal_assistant_app.models import NlgTemplates
from personal_assistant_app.models import NlgLog
from rest_framework import serializers


class ActionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actions
        fields = [
            'action_id',
            'timestamp'
            ]

class ActionLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActionLog
        fields = [
            'request_json',
            'response_json',
            ]

class ConversationLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConversationLog
        fields = [
            'conversation_id',
            'from_user',
            'to_user',
            'timestamp'
            ]

class NlgLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NlgLog
        fields = [
            'conversation_id',
            'request_json',
            'response_json',
            'timestamp'
            ]

class NlgTemplatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NlgTemplates
        fields = [
            'conversation_id',
            'response_id',
            'text',
            'buttons',
            'image',
            'elements',
            'attachments',
            'timestamp'
            ]
