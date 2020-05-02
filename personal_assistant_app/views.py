from django.shortcuts import render
from personal_assistant_app.models import ConversationLog
from personal_assistant_app.serializers import ConversationLogSerializer
from personal_assistant_app.serializers import FromUserSerializer
from personal_assistant_app.serializers import FromAssistantSerializer
from personal_assistant_app.webhook import post_message
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from datetime import date
import random
import math
import json

# Create your views here.
def index(request):

    queryset_log = ConversationLog.objects.all().order_by('timestamp')
    serializer_class_log = ConversationLogSerializer(queryset_log, many=True)


    context = {
        'json_conversation_log': json.dumps(serializer_class_log.data),
    }


    return render(request, 'personal_assistant_app/index.html', context)

class ConversationLogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ConversationLog.objects.all().order_by('timestamp')
    serializer_class = ConversationLogSerializer
    permission_classes = [permissions.AllowAny]

class FromUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        r = post_message("test","hello")
        return r

    def get_serializer_class(self):
        return FromAssistantSerializer