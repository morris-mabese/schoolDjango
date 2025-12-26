from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"), 
    path('classes.html', views.classes, name="classes"), 
    path('teachers.html', views.teachers, name="teachers"), 
    path('career.html', views.career, name="career"), 
    path('facility.html', views.facility, name="facility"), 
    path('testimonial.html', views.testimonial, name="testimonial"), 
    path('contact.html', views.contact, name="contact"), 
    path('departmental-heads.html', views.departmental_heads, name="departmental-heads"), 
    path('vacancy.html', views.vacancy, name="vacancy"),
    path('requirement.html', views.requirement, name="requirement"),
    path('history.html', views.history, name="history"),
    path('managing-director-message.html', views.managing_director_message, name="managing-director-message"),
    path('bod-message.html', views.bod_message, name="bod-message"),
    path('fees-structure.html', views.fees_structure, name="fees-structure"),
    
    
    
    
]

