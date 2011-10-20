from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=50)
    students = models.IntegerField(default=28)

    
class SchoolLevel(models.Model):
    name = models.CharField(max_length=50)

class School(models.Model):
    name = models.CharField(max_length=50)

class SchoolLeveling(models.Model):
    school = models.ForeignKey(School)
    level = models.ForeignKey(SchoolLevel)

