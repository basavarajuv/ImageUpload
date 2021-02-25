from django.contrib import admin

from .models import MyModelName, UploadFiles

class AdminModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'salary', 'location', 'email']

admin.site.register(MyModelName, AdminModel)

class AdminUpload(admin.ModelAdmin):
    list_display = ['id', 'category', 'image_file']

admin.site.register(UploadFiles, AdminUpload)
