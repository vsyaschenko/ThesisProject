from django.contrib import admin

from .models import Selections, Problems, Solutions

class SelectionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    list_display_links = ('title',)
    search_fields = ('title', 'parent')

class ProblemsAdmin(admin.ModelAdmin):
    list_display = ('title', 'selection')
    list_display_links = ('title',)
    search_fields = ('title', 'selection', 'content')

class SolutionsAdmin(admin.ModelAdmin):
    list_display = ('problem',)
    list_display_links = ('problem',) #Без запятой воспринимает как стрку WTF
    search_fields = ('problem', 'content')

# Register your models here.
admin.site.register(Selections, SelectionsAdmin)
admin.site.register(Problems, ProblemsAdmin)
admin.site.register(Solutions, SolutionsAdmin)