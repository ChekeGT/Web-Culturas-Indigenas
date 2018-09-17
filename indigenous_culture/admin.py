from django.contrib import admin
from  .models import Culture, Dict, Word

# Register your models here.
class Admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Culture, Admin)
admin.site.register(Dict, Admin)
admin.site.register(Word, Admin)