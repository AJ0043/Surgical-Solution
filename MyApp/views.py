from django.shortcuts import render
from .models import TestimonialCard
from .models import GalleryPhoto,Blog


# Create your views here.

def Home(request):
    return render(request,'index.html')


def Treatment(request):
    return render(request,'Treatment.html')


def Lapro(request):
    return render(request,'Lapro.html')

def Anorc(request):
    return render(request,'Anorctal.html')

def lap(request):
    return render(request,'Lap.html')

def Breast(request):
    return render(request,'Breast.html')

def Stapler(request):
    return render(request,'Stapler.html')

def Procto(request):
    return render(request,'Procto.html')

def Consol(request):
    return render(request,'Consol.html')

def Diag(request):
    return render(request,'Diag.html')

def Treat(request):
    return render(request,'Treat.html')

def Surgury(request):
    return render(request,'Surgury.html')

def Recovery(request):
    return render(request,'Recovery.html')

def Feedback(request):
    return render(request,'Feedback.html')

def Test(request):
    testimonials = TestimonialCard.objects.all()
    return render(request, 'Testimonial.html', {'testimonials': testimonials})

def gallery_view(request):
    photos = GalleryPhoto.objects.all()
    return render(request, 'gallery.html', {'photos': photos})


def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog.html', {'blogs': blogs})


def About(request):
    return render(request,"about.html")



def Contact(request):
    return render(request,"Contact.html")


def Book(request):
    return render(request,"Book.html")

def Html(request):
    return render(request,"html.html")