from django.contrib import admin
from .models import StuBook,Student,StuReview

# Register your models here.
admin.site.register(Student)
admin.site.register(StuBook)
admin.site.register(StuReview)