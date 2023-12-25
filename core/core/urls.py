from django.urls import path, include
from . import views 

urlpatterns = [
    path('', view=views.home, name="home"),
    path('explore', view=views.explore, name="explore"),
    path('about', view=views.about, name="about"),
    path('contact', view=views.contact, name="contact"),
    path('profile', view=views.profile, name="profile"),
    path('event/<str:pk>', view=views.event, name="event"),
    path('alert', view=views.alert, name='alert'),
    path('login', view=views.login_, name='login'),
    path('register', view=views.register_user, name='register_user'),
    path('logout', view=views.logout_, name='logout'),
]
