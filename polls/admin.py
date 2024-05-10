from django.contrib import admin
from django.utils.safestring import mark_safe

from polls.models import News, Category


@admin.register(News)
class NewAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'category', 'created_at', 'status', 'get_image')
    list_display_links = ("id", 'title',)
    list_filter = ('category__title', 'created_at', 'author', 'status')
    search_fields = ('title', 'author', 'category__title',)
    readonly_fields = ('get_image',)
    save_on_top = True
    list_editable = ('status',)
    fieldsets = (
        ('Categories', {
            'fields': (('category', 'additional_category'),)
        }),
        ('Title and Slug', {
            'fields': (('title', 'slug'),)
        }),
        ('Author and status', {
            'fields': (('author', 'status'),)
        }),
        ('Date and Picture', {
            'fields': (('picture', 'get_image'),)
        }),
        ('', {
            'fields': ("created_at", ),
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.picture.url} width="90" height="70"')

    get_image.short_description = 'Picture'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Categories """

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)
