
from django.contrib import admin
from .models import Teacher, Course, Student


# =====================================================
# ADMINISTRACIÓN DE TEACHER
# =====================================================

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'fullname',
        'email',
        'specialty',
        'age',
        'is_active',
    )

    list_filter = (
        'is_active',
        'specialty',
    )

    search_fields = (
        'fullname',
        'email',
        'specialty',
    )


# =====================================================
# ADMINISTRACIÓN DE COURSE
# =====================================================

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'credits',
        'is_active',
    )

    list_filter = (
        'is_active',
        'credits',
    )

    search_fields = (
        'name',
        'description',
    )


# =====================================================
# ADMINISTRACIÓN DE STUDENT
# =====================================================

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'fullname',
        'email',
        'age',
        'career',
        'is_active',
    )

    list_filter = (
        'is_active',
        'career',
    )

    search_fields = (
        'fullname',
        'email',
        'career',
    )
