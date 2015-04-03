from django.contrib import admin

# Register your models here.
from .models import Abhyasi, Sitting

class SittingInline(admin.TabularInline):
	model = Sitting
	extra = 1

class AbhyasiAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 					{'fields':['name', 'date_of_birth', 'date_of_join', 'id_card_number', 'address']}),
		('Sitting information', {'fields':['date_of_birth'], 'classes':['collapse']})
	]

admin.site.register(Abhyasi, AbhyasiAdmin)