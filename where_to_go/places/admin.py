from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image

    readonly_fields = ["get_preview", ]
    list_display = ['img', 'get_preview', 'position']

    def get_preview(self, obj):
        return format_html('<img src="{}" height="{}" />',
                           obj.img.url,
                           '200px',
                           )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline, ]
    search_fields = ['title']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ["get_preview", ]
    list_display = ['img', 'place', 'get_preview']

    def get_preview(self, obj):
        return format_html('<img src="{}" height="{}" />',
                           obj.img.url,
                           '150px',
                           )
