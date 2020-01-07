from django.contrib import admin

from .models import Section, Processes, Problems, Solutions

# Register your models here.
admin.site.register(Section)
admin.site.register(Processes)
admin.site.register(Problems)
admin.site.register(Solutions)
