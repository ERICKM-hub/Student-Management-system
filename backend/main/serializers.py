from rest_framework import serializers
from .models import *

class userProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=[
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'role',
            'location',
            'is_active',
            'is_superuser',
        ]