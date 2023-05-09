from django.contrib import admin

from .models import DBInstance, DBInstanceBackup, DBInstanceNode, Project, User

# Register your models here.
admin.site.register(DBInstance)
admin.site.register(DBInstanceNode)
admin.site.register(DBInstanceBackup)
admin.site.register(Project)
admin.site.register(User)

