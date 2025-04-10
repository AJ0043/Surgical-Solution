from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),  # Example route
    path('Treatment/', views.Treatment, name='Treatment'),  # Example route
    path('Lapro/', views.Lapro, name='Lapro'),
    path('Anorc/', views.Anorc, name='Anorc'),
    path('Lap/', views.lap, name='Lap'),
    path('Breast/', views.Breast, name='Breast'),
    path('Stepler/', views.Stapler, name='stepler'),
    path('Procto/', views.Procto, name='Procto'),
    path('Consultation/', views.Consol, name='Consol'),
    path('Diagonsis/', views.Diag, name='Diagonsis'),
    path('Treat/', views.Treat, name='Treat'),
    path('Surgury/', views.Surgury, name='Surgury'),
    path('Recovery/', views.Recovery, name='Recovery'),    
    path('Feedback/', views.Feedback, name='Feedback'),
    path('Test/', views.Test, name='Testmonial'),    
    path('gallery/', views.gallery_view, name='gallery'),   
    path('blogs/', views.blog_list, name='blog_list'), 
    path('About/', views.About, name='About'), 
    path('Contact/', views.Contact, name='Contact'), 
    path('Book/', views.Book, name='Book'),
        
        
        
]
