from django.urls import path
from myApp import views
from .views import class_view
urlpatterns = [
    path('', views.home, name='homepage' ),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('add_note/', views.add_note, name='add_note'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('class/', class_view.as_view(), name='class'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)