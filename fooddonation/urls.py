from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('orphanage/', views.orphanage, name='orphanage'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('superadmin/', views.superadmin, name='superadmin'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('people/', views.people, name='people'),
    path('addrestaurant/', views.addrestaurant, name='addrestaurant'),
    path('addorphanage/', views.addorphanage, name='addorphanage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)