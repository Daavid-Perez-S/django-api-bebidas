from rest_framework import serializers
from .models import Bebidas

class BebidasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bebidas
        fields = ('id', 'name', 'description', 'image_url')

    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)
    image_url = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Bebidas.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.image_url = validated_data.get('image_url', instance.image_url)

        instance.save()
        return instance