from django.conf.urls import url, include
from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from membership.models import PJUser


class PJUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:

        model = PJUser
        fields = ('id', 'email',
                  'first_name', 'last_name', 'password',
                  'confirm_password','bio','skills','majors')
        read_only_fields = ('created_at', 'updated_at',)

        def create(self, validated_data):
            return PJUser.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.email = validated_data.get('email', instance.email)
            instance.tagline = validated_data.get('tagline', instance.tagline)

            instance.save()

            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
                instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

            return instance