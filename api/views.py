from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

def home(request):
    return render(request, 'home.html')

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'username': 'Ivar',
            'age': 10
        }
        return Response(data)