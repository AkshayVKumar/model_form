from django.contrib import admin
from myapp.models import *
# Register your models here.
class WebpageAdmin(admin.ModelAdmin):
    list_display=('topic','name','url')
    list_per_page=5
    list_editable=('url',)
    search_fields=('topic__name',)
    list_filter=('topic',)
admin.site.register(Topic)
admin.site.register(Webpage,WebpageAdmin)
admin.site.register(Access_Records)