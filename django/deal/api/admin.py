from django.contrib import admin
from .models import sample

# Register your models here.
class sampleAdmin(admin.ModelAdmin):
    pass
admin.site.register(sample,sampleAdmin)
#admin.site.register(Device,DeviceAdmin)


# admin header and title modification
admin.site.site_header = "Admin DashBoard"
admin.site.site_title = "Azure test"
admin.site.index_title = 'Welcome To test Portal'
