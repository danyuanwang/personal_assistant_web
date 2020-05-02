from personal_assistant_app.models import ConversationLog
from rest_framework import serializers


class ConversationLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConversationLog
        fields = ['from_user']