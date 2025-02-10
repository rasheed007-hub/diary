from rest_framework import serializers
from .models import Diary


class DiarySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = '__all__'
