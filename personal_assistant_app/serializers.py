from personal_assistant_app.models import ConversationLog
from rest_framework import serializers


class ConversationLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConversationLog
        fields = [
            'conversation_id',
            'from_user',
            'to_user',
            'timestamp'
            ]
