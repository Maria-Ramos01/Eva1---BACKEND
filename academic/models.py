
from django.db import models


# =====================================================
# MODELO TEACHER
# =====================================================
class Teacher(models.Model):

    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    specialty = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.fullname


# =====================================================
# MODELO COURSE
# =====================================================
class Course(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    credits = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# =====================================================
# MODELO STUDENT
# =====================================================
class Student(models.Model):

    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveSmallIntegerField()
    career = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.fullname
