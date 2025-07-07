from django.contrib import admin
from .models import Category, Course

admin.site.site_header = "Admin Panel"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome to admin panel"


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price')


class CoursesInline(admin.TabularInline):
    model = Course
    exclude = ('created_at',)
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapse']
        })
    ]
    inlines = [CoursesInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
