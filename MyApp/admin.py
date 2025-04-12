from django.contrib import admin
from .models import TestimonialCard
from .models import GalleryPhoto,Blog,Testimonial,Contact ,Appointment

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

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('Name2', 'Email2', 'Subject2', 'phone2')  # admin panel mein ye columns dikhayenge
    search_fields = ('Name2', 'Email2', 'Subject2')  



@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'city', 'phone', 'surgery', 'date_created')
    search_fields = ('name', 'city', 'phone', 'surgery')
    list_filter = ('surgery', 'date_created')