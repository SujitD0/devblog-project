from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('post-list-api/', views.post_list_api, name='post-list-api'),
    path('post-detail-api/<int:pk>/', views.post_detail_api, name='post_detail_api'),
]