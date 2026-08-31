
from rest_framework import serializers
from .models import Teacher, Course, Student


# =====================================================
# SERIALIZER DE TEACHER
# =====================================================
# Convierte los objetos Teacher de Django a JSON
# y permite recibir datos JSON para crear/modificar
# profesores.

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher

        # '__all__' incluye todos los campos
        # definidos en el modelo Teacher.
        fields = '__all__'


# =====================================================
# SERIALIZER DE COURSE
# =====================================================
# Convierte los objetos Course a JSON y permite
# crear/modificar cursos mediante la API.

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course

        # Incluye todos los campos del modelo Course.
        fields = '__all__'


# =====================================================
# SERIALIZER DE STUDENT
# =====================================================
# Convierte los objetos Student a JSON y permite
# crear/modificar estudiantes mediante la API.

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student

        # Incluye todos los campos del modelo Student.
        fields = '__all__'
