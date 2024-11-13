from django.shortcuts import render

# Create your views here.
# myapp/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import YourModel
from .serializers import YourModelSerializer


class YourDataView(APIView):
    def get(self, request):
        # Retrieve data from the database
        data = YourModel.objects.all()

        # Serialize the data using the serializer
        serializer = YourModelSerializer(data, many=True)

        # Return the serialized data as a Response
        return Response(serializer.data)
