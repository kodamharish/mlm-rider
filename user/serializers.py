# riders/serializers.py
from rest_framework import serializers
from .models import Rider


class RiderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rider
        fields = '__all__'

    def validate_vehicle_number(self, value):
        if Rider.objects.filter(vehicle_number=value).exists():
            raise serializers.ValidationError("Vehicle number already exists")
        return value

    def validate_aadhaar_number(self, value):
        if len(value) != 12 or not value.isdigit():
            raise serializers.ValidationError("Aadhaar must be 12 digits")
        return value

    def validate_pincode(self, value):
        if len(value) != 6:
            raise serializers.ValidationError("Pincode must be 6 digits")
        return value