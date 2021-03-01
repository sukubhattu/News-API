from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import News


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = News
