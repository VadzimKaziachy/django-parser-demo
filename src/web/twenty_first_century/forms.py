from rest_framework import serializers


class BodySerializer(serializers.Serializer):
    code = serializers.CharField()
    price = serializers.CharField()
    name = serializers.CharField()
