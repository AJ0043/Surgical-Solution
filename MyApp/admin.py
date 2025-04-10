from django.contrib import admin
from .models import TestimonialCard
from .models import GalleryPhoto,Blog,Testimonial

@admin.register(TestimonialCard)
class TestimonialCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'facebook', 'twitter', 'instagram')


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']  




@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'message', 'facebook', 'instagram', 'image']  # Yahin error hai

admin.site.register(Testimonial, TestimonialAdmin)