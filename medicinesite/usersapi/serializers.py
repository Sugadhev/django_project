from rest_framework import serializers
from users.models import RegisterForm


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterForm
        fields = "__all__"