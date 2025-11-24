from django.urls import path

from myapp import views

urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('donation/', views.donation, name='donation'),
path('event/', views.event, name='event'),
path('feature/', views.feature, name='feature'),
path('service/', views.service, name='service'),
path('team/', views.team, name='team'),
path('testimonial/', views.testimonial, name='testimonial'),

]