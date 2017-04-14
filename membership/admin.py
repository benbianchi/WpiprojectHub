from django.contrib import admin
from .project.models import Project, Skill, Major
# Register your models here.

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Major)