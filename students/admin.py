from django.contrib import admin
from .models import StudentProfile, Batch, FeeRecord

# Register your models so they appear in the admin panel
admin.site.register(StudentProfile)
admin.site.register(Batch)
admin.site.register(FeeRecord)
