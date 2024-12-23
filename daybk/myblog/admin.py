from django.contrib import admin
from .models import Post, Task, Plan


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ['title']}

class TaskAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ['name']}
    
class PlanAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Plan, PlanAdmin)

