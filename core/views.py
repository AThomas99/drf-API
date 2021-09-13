from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    def get(self, request, format=None):
        data = {
            'name': 'John Doe',
            'age': 23
        }
        return Response(data)