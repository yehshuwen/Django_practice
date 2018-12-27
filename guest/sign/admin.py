from django.contrib import admin
from sign.models import Event, Guest

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['id','name','status','address','start_time']
    search_fields = ['name'] #搜尋方塊
    list_filter = ['status'] #篩選程式

class GuestAdmin(admin.ModelAdmin):
    list_display = ['event','realname','phone','email','sign','create_time']
    search_fields = ['realname','phone'] #搜尋方塊
    list_filter = ['sign'] #篩選程式

admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)
