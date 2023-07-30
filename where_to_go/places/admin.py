from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html


class ImageInline(admin.TabularInline):
    model = Image

    readonly_fields = ["get_preview", ]
    fields = ['img', 'get_preview', 'img_position']

    def get_preview(self, obj):
        return format_html('<img src="{}" width="{}" height={} />',
                           obj.img.url,
                           f'{(obj.img.width / obj.img.height) * 200}px',
                           '200px',
                           )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


admin.site.register(Image)
