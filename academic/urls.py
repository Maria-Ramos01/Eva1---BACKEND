from django.urls import path, include
from rest_framework import routers
from academic import views


# =====================================================
# ROUTER DE DJANGO REST FRAMEWORK
# =====================================================
# DefaultRouter crea automáticamente las rutas
# correspondientes a nuestros ViewSet.

router = routers.DefaultRouter()


# =====================================================
# ENDPOINT DE CURSOS
# =====================================================
# Permite acceder a los cursos mediante:
# /api/courses/

router.register(
    r'courses',
    views.CourseViewSet
)


# =====================================================
# ENDPOINT DE ESTUDIANTES
# =====================================================
# Permite acceder a los estudiantes mediante:
# /api/students/

router.register(
    r'students',
    views.StudentViewSet
)


# =====================================================
# URLPATTERNS DE LA API
# =====================================================
# Incluimos todas las rutas generadas automáticamente
# por DefaultRouter.

urlpatterns = [
    path(
        '',
        include(router.urls)
    ),
]
