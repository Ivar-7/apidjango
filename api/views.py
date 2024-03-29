from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated

from .serializers import StudentSerializer
from .models import Student

def home(request):
    return render(request, 'home.html')

class TestView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        qs = Student.objects.all()
        # student1 = qs.first()
        # serializer = StudentSerializer(qs)
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
