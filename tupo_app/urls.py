from email.mime import image
from django.urls import path
from tupo_app import views

app_name ='tupo_app'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('credit/', views.credit, name='credit'),
    path('emytology/', views.emytology, name='emytology'),
    
    path('community/', views.Comm.as_view(), name='community'),

    path('award/', views.award, name='award'),
]