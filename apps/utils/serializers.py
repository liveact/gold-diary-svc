from django.contrib import auth
from rest_framework import serializers


class SetUserSerializerMixin:
    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["user_id"] = request.user.id
        return super().create(validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=32)
    password = serializers.CharField(max_length=32)

    def create(self, validated_data):
        user = auth.authenticate(**validated_data)
        if user:
            auth.login(self.context.get("request"), user)
            return user
        else:
            raise serializers.ValidationError("password incorrect.", code=401)
