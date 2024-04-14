from django.contrib import admin

# Register your models here.


from .models import *


admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Attempt)
admin.site.register(Resource)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(CheatSheet)