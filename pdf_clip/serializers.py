# serializers.py
from rest_framework import serializers

from .models import Clip, File

class ClipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clip
        fields = ('fileId', 'clipNumber', 'pageNumber', 'minY', 'maxY', 'minX', 'maxX', 'note')

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'fileName', 'positionArray', 'maxPageHeight', 'maxPageWidth')