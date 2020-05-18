from django.shortcuts import render
from personal_assistant_app.models import Actions
from personal_assistant_app.models import ActionLog
from personal_assistant_app.models import ConversationLog
from personal_assistant_app.models import NlgTemplates
from personal_assistant_app.models import NlgLog
from personal_assistant_app.serializers import ActionsSerializer
from personal_assistant_app.serializers import ActionLogSerializer
from personal_assistant_app.serializers import ConversationLogSerializer
from personal_assistant_app.serializers import NlgLogSerializer
from personal_assistant_app.serializers import NlgTemplatesSerializer
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


@api_view(['POST'])
@permission_classes([AllowAny])
def take_action(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        action_request = request.data
        action_response = {
            'events': 
            [
                {'event': 'form', 'name': 'ask_disease_data_form', 'timestamp': None}, 
                {'event': 'slot', 'timestamp': None, 'name': 'disease', 'value': 'covid-19'}, 
                {'event': 'slot', 'timestamp': None, 'name': 'treatment', 'value': 'died'}, 
                {'event': 'slot', 'timestamp': None, 'name': 'disease', 'value': 'covid-19'}, 
                {'event': 'slot', 'timestamp': None, 'name': 'treatment', 'value': ['died', 'died']}, 
                {'event': 'slot', 'timestamp': None, 'name': 'requested_slot', 'value': 'GPE'}
            ], 
            'responses': 
            [
                {
                    'text': None, 
                    'buttons': [], 
                    'elements': [], 
                    'custom': {}, 
                    'template': 'utter_ask_GPE', 
                    'image': None, 
                    'attachment': None, 
                    'GPE': None, 
                    'amount': None, 
                    'area': None, 
                    'city': None, 
                    'country': None, 
                    'county': None, 
                    'disease': 'covid-19', 
                    'location': None, 
                    'province': None, 
                    'requested_slot': None, 
                    'state': None, 
                    'time': None, 
                    'town': None, 
                    'treatment': ['died', 'died']
                    }
                ]
            }

        if from_user is not None:
            al = ActionLog(
               request_json=json.dumps(action_request),
               response_json=json.dumps(action_response)
           )
            
            al.save()
            
            return Response(action_response, status=status.HTTP_200_OK)

        return Response("no data in request", status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def generate_nl(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        nlg_request = request.data
        if from_user is not None:
            nlg_response = {
                "text": "which place?",
                "buttons": [],
                "image": None,
                "elements": [],
                "attachments": []
            }

            conversation_id = nlg_request["tracker"]["sender_id"]

            nl = NlgLog(
                conversation_id=conversation_id,
                request_json = json.dumps(nlg_request),
                response_json=json.dumps(nlg_response),
            )
            nl.save()

            return Response(nlg_response, status=status.HTTP_200_OK)

        return Response("no data in request", status=status.HTTP_400_BAD_REQUEST)
