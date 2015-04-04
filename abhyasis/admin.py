from django.contrib import admin

# Register your models here.
from .models import Abhyasi, Sitting

class SittingInline(admin.TabularInline):
	model = Sitting
	extra = 3

class AbhyasiAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {
				'fields':['name', 'biography', ]
				}
			),
		('More information', {
			'fields':['date_of_birth', 'date_of_join', 'id_card_number', 'address'], 
			'classes':['collapse']})
	]
	inlines = [SittingInline]

admin.site.register(Abhyasi, AbhyasiAdmin)