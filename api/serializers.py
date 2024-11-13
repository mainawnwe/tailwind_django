# myapp/serializers.py

from rest_framework import serializers
from .models import YourModel


class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModel  # Replace this with your model
        fields = "__all__"  # Or specify a list of fields you want to include
