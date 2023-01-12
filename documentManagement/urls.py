from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name= "DMS"),
    path('document-registration/', views.documentRegistration, name = "documentRegistration"),
    path('document-edit/<str:pk>', views.documentEdit, name = "documentEdit"),
    path('delete/<str:pk>', views.deleteDocument, name ="deleteForm"),
    path('update-distribution/<str:pk>', views.updateDistribution, name='updateDistribution'),
    path('view-pdf/<str:pk>',views.viewDocument, name='viewPDF'),
    ]

