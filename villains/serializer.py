from rest_framework import serializers
from .models import Villain

class villainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Villain
        fields = ('id', 'author', 'name','show_name', 'desc', 'created_at', 'updated_at') 