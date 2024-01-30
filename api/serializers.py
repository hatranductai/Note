from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
        extra_kwargs = {"body": {"trim_whitespace": False, "allow_blank": True}}
