from django.shortcuts import render,redirect
from .models import TestimonialCard
from .models import GalleryPhoto,Blog
from .models import Testimonial , Contact ,Appointment
from django.contrib import messages
from django.contrib import messages


# Create your views here.

def Home(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        surgery = request.POST.get('surgery')
        message_text = request.POST.get('message')

        Appointment.objects.create(
            name=name,
            age=age,
            city=city,
            phone=phone,
            surgery=surgery,
            message=message_text
        )

        messages.success(request, '🎉 Your appointment has been booked successfully!')
        return redirect('home')

     testimonials = Testimonial.objects.all()

     return render(request, 'index.html', {
        'testimonials': testimonials

    })

def Treatment(request):
    return render(request,'Treatment.html')


def Lapro(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        surgery = request.POST.get('surgery')
        message_text = request.POST.get('message')

        Appointment.objects.create(
            name=name,
            age=age,
            city=city,
            phone=phone,
            surgery=surgery,
            message=message_text
        )

        messages.success(request, '🎉 Your appointment has been booked successfully!')
        return redirect('Lapro')

    return render(request, 'Lapro.html')  # Or 'Store/Inc/con.html' if that's the form

    

def Anorc(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        surgery = request.POST.get('surgery')
        message_text = request.POST.get('message')

        Appointment.objects.create(
            name=name,
            age=age,
            city=city,
            phone=phone,
            surgery=surgery,
            message=message_text
        )

        messages.success(request, '🎉 Your appointment has been booked successfully for Anorctal Surgury!')
        return redirect('Anorc')

    return render(request, 'Anorctal.html')  # Or 'Store/Inc/con.html' if that's the form

   
    

def lap(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        surgery = request.POST.get('surgery')
        message_text = request.POST.get('message')

        Appointment.objects.create(
            name=name,
            age=age,
            city=city,
            phone=phone,
            surgery=surgery,
            message=message_text
        )

        messages.success(request, '🎉 Your appointment has been booked successfully ')
        return redirect('Lap')

     return render(request, 'Lap.html')  # Or 'Store/Inc/con.html' if that's the form



def Breast(request):
 if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        surgery = request.POST.get('surgery')
        message_text = request.POST.get('message')

        Appointment.objects.create(
            name=name,
            age=age,
            city=city,
            phone=phone,
            surgery=surgery,
            message=message_text
        )

        messages.success(request, '🎉 Your appointment has been booked successfully ')
        return redirect('Breast')

 return render(request, 'Breast.html')  # Or 'Store/Inc/con.html' if that's the form

   
   
   
   

def Stapler(request):
   
   if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        surgery = request.POST.get('surgery')
        message_text = request.POST.get('message')

        Appointment.objects.create(
            name=name,
            age=age,
            city=city,
            phone=phone,
            surgery=surgery,
            message=message_text
        )

        messages.success(request, '🎉 Your appointment has been booked successfully ')
        return redirect('stepler')

   return render(request, 'Stapler.html')  # Or 'Store/Inc/con.html' if that's the form

   
   
   

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
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        facebook = request.POST.get('facebook')
        instagram = request.POST.get('instagram')
        image = request.FILES.get('image')  # ✅ For file upload

        if not name or not message:
            messages.error(request, 'Name and message are required!')
            return redirect('Testmonial')

        try:
            testimonial = Testimonial(
                name=name,
                message=message,
                facebook=facebook,
                instagram=instagram
            )

            if image:
                testimonial.image = image  # ✅ Save image if present

            testimonial.save()
            messages.success(request, 'Thank you for your feedback!')

        except Exception as e:
            print("Error while saving testimonial:", e)
            messages.error(request, 'Something went wrong while saving your feedback.')

        return redirect('Testmonial')

    # GET request – fetch all testimonials to show on the page
    testimonials = Testimonial.objects.all().order_by('-id')
    return render(request, 'Testimonial.html', {'testimonials': testimonials})




def gallery_view(request):
    photos = GalleryPhoto.objects.all()
    return render(request, 'gallery.html', {'photos': photos})


def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog.html', {'blogs': blogs})


def About(request):
    return render(request,"about.html")



def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('Name2')
        email = request.POST.get('Email2')
        subject = request.POST.get('Subject2')
        phone = request.POST.get('phone2')
        message = request.POST.get('Message2')

        # Save to database
        Contact.objects.create(
            Name2=name,
            Email2=email,
            Subject2=subject,
            phone2=phone,
            Message2=message
        )

        messages.success(request, "Thanks for contacting us! We'll get back to you soon.")
        return redirect('contact')

    return render(request, "Contact.html")











def Book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        surgery = request.POST.get('surgery')
        message_text = request.POST.get('message')

        Appointment.objects.create(
            name=name,
            age=age,
            city=city,
            phone=phone,
            surgery=surgery,
            message=message_text
        )

        messages.success(request, '🎉 Your appointment has been booked successfully!')
        return redirect('Book')

    return render(request, 'Book.html')  # Or 'Store/Inc/con.html' if that's the form

   




def Html(request):
    return render(request,"html.html")



#### Views.py ######

def feedback_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        facebook = request.POST.get('facebook')
        instagram = request.POST.get('instagram')

        Testimonial.objects.create(
            name=name,
            message=message,
            facebook=facebook,
            instagram=instagram
        )

        messages.success(request, 'Thank you for your feedback!')
        return redirect('Testmonial')

    return render(request, 'Testimonial.html')


