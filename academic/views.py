
from django.shortcuts import render
from rest_framework import viewsets
from .serializer import TeacherSerializer
from .serializer import CourseSerializer
from .serializer import StudentSerializer
from .models import Teacher, Course, Student

# Create your views here.

# =====================================================
# VISTA PRINCIPAL
# =====================================================

def home(request):
    """
    Vista utilizada para la ruta principal "/".

    Renderizamos courses.html para evitar que
    Django muestre un error 404 al ingresar a:
    http://127.0.0.1:8000/
    """

    return render(
        request,
        'academic/courses.html'
    )


# =====================================================
# VISTA DE CURSOS
# =====================================================

def courses(request):
    """
    Renderiza la página HTML de cursos.

    Los datos NO se envían directamente desde
    esta vista.

    JavaScript utilizará fetch() para obtenerlos
    desde /api/courses/.
    """

    return render(
        request,
        'academic/courses.html'
    )


# =====================================================
# VISTA DE ESTUDIANTES
# =====================================================

def students(request):
    """
    Renderiza la página HTML de estudiantes.

    Los estudiantes serán obtenidos posteriormente
    mediante fetch() desde /api/students/.
    """

    return render(
        request,
        'academic/students.html'
    )

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer