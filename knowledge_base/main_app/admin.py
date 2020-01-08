from django.contrib import admin

from .models import Sections, Processes, Problems, Solutions, Settings

# Register your models here.
admin.site.register(Sections)
admin.site.register(Processes)
admin.site.register(Problems)
admin.site.register(Solutions)
admin.site.register(Settings)
