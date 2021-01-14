from django.contrib import admin
from .models import advertisment,contactmodel,extenduser
# Register your models here.
@admin.register(advertisment)
class advertisment(admin.ModelAdmin):
    list_display=['title','description','img','category','user','date']

@admin.register(contactmodel)
class contactmodel(admin.ModelAdmin):
    list_display=['id','email','subject']
admin.site.register(extenduser)



