from rest_framework import serializers
from myapp.models import Items
from django.db.models import fields

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Items
        fields='__all__'