from django.db import models
from django.contrib import admin


class DBInstance(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class DBInstanceNode(models.Model):
    name = models.CharField(max_length=50)
    db_instance = models.ForeignKey(DBInstance, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class DBInstanceBackup(models.Model):
    name = models.CharField(max_length=50)
    db_instance = models.ForeignKey(DBInstance, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField('User')

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=50)
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.name