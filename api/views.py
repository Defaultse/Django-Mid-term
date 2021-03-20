from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from api.serializers import *


class BookViewSet(viewsets.ViewSet, viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass

    def get_permissions(self):
        if self.action == 'book':
            permission_classes = (IsAdminUser,)
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return Book.objects.all()

    def book(self, request):
        serializer = BookSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class JournalViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    serializer_class = JournalSerializer

    def get_permissions(self):
        if self.action == 'journal':
            permission_classes = (IsAdminUser,)
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return Journal.objects.all()

    def journal(self, request):
        serializer = JournalSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)