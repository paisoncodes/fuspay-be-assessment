from rest_framework import serializers

from items.models import CrudItem



class CrudItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrudItem
        fields = "__all__"