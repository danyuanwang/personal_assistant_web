from personal_assistant_app.models import ConversationLog, FromAssistant, FromUser
from rest_framework import serializers


class ConversationLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConversationLog
        fields = ['from_user']

class FromUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FromUser
        fields = ['sender', "message"]

class FromAssistantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FromAssistant
        fields = ["recipient_id", "text"]