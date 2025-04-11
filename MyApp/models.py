from django.db import models

class TestimonialCard(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonial_images/')
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name




class GalleryPhoto(models.Model):
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return f"Photo {self.id}"
    

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs/')
    button_text = models.CharField(max_length=50, default='Read More')
    button_link = models.URLField(blank=True, null=True)  # Optional button URL
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    
    



# models For Feedback ####
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to='Testimonial/', blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
   
