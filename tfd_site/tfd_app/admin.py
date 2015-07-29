from django.contrib import admin

from .models import Type, Strain

# Register your models here.


class ChoiceInLine(admin.TabularInline):
    model = Strain
    extra = 2


class TypeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Strain Type', {'fields':['type_text'], 'classes': ['collapse']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]

    list_display = ('type_text', 'pub_date', 'was_published_recently')
    list_filter = ['type_text', 'pub_date']
    search_fields = ['type_text']


admin.site.register(Type, TypeAdmin)
admin.site.register(Strain)