from django.shortcuts import render
from personal_assistant_app.models import ConversationLog
from personal_assistant_app.serializers import ConversationLogSerializer
from personal_assistant_app.webhook import post_message
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
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


@api_view(['POST'])
@permission_classes([AllowAny])
def from_user(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        from_user = request.data
        if from_user is not None:
            conversation_id = from_user["sender"]
            from_user = from_user["message"]
            c = ConversationLog(
                conversation_id=conversation_id, from_user=from_user, to_user="")
            c.save()
            from_assistant = post_message(conversation_id, from_user)

            conversation_id = from_assistant[0]["recipient_id"]
            to_user = from_assistant[0]["text"]
            d = ConversationLog(
                conversation_id=conversation_id, from_user="", to_user=to_user)
            d.save()

            return Response(json.dumps(from_assistant), status=status.HTTP_200_OK)

        return Response("no data in request", status=status.HTTP_400_BAD_REQUEST)
