from django.contrib import admin
from models import *
# Register your models here.
class singleInformationAdmin(admin.ModelAdmin):
	list_display = ('admin_Aboutimage', 'aboutText_es', 'published',)
	list_display_links = ('admin_Aboutimage', 'aboutText_es',)
	list_editable = ('published',)
	ordering = ('id',)

class proyectAdmin(admin.ModelAdmin):
	fields = ['name_es', 'description_es', 'name_en', 'description_en', 'mainImage', 'secondImage', 'imageOrientation', 'published']
	list_display = ('name_es', 'description_es', 'admin_image', 'imageOrientation', 'published', 'pub_date')
	list_display_links = ('name_es', 'description_es', 'admin_image', 'pub_date')
	list_editable = ('imageOrientation', 'published')
	ordering = ('pub_date',)

class imageAdmin(admin.ModelAdmin):
	list_display = ('name', 'admin_image', 'imageOrientation', 'proyect')
	list_display_links = ('name', 'admin_image', 'proyect')
	list_editable = ('imageOrientation',)
	ordering = ('proyect',)

class pressAdmin(admin.ModelAdmin):
	list_display = ('name_es', 'admin_image', 'description_es', 'pub_date')
	list_display_links = ('name_es', 'admin_image', 'description_es', 'pub_date')
	ordering = ('pub_date',)

admin.site.register(singleInformation, singleInformationAdmin)
admin.site.register(Proyect, proyectAdmin)
admin.site.register(Image, imageAdmin)
admin.site.register(Press, pressAdmin)