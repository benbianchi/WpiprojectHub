from django.conf.urls import url, include
from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):


    class Meta:

        model = Project
        fields = ('projectAuthor', 'projectName',
                  'projectTagLine', 'projectDescription', 'projectMajor',
                  'projectSkills','postDate','projectBeginDate','projectEndDate','projectDuration')
        read_only_fields = ('created_at', 'updated_at',)

        def create(self, validated_data):
            return Project.objects.create(**validated_data)

        def update(self, instance, validated_data):
            #TODO
            return instance