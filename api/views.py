from django.shortcuts import render
from rest_framework import viewsets
from .models import Group, Event
from .serializers import GroupSerializer, EventSerializer, GroupFullSerializer
from rest_framework.response import Response
# Create your views here.

class GroupViewsets(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = GroupFullSerializer(instance, many=False, context={"request":request})
        return Response(serializer.data)

class EventViewsets(viewsets.ModelViewSet):
        queryset = Event.objects.all()
        serializer_class = EventSerializer

