from django.contrib import admin

from photos.models import Photo


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_tagged_pets', 'date_of_publications', 'description']


    def get_tagged_pets(self, obj):
        return ', '.join(p.name for p in obj.tagged_pets.all())

