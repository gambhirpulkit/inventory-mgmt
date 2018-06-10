from rest_framework import serializers
from .models import Boxes


class BoxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boxes
        fields = ('type', 'length', 'breadth', 'height')