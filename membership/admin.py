from django.contrib import admin
from .models import Project, Member, Skill, Major
# Register your models here.

admin.site.register(Project)
admin.site.register(Member)
admin.site.register(Skill)
admin.site.register(Major)