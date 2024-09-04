from django.urls import path,include
from . import views


urlpatterns=[
    path("Signout/", views.signout, name="Signout"),
      path('signup/', views.signup, name='signup'),
    path("", views.signin, name="signin"),
    path("first/",views.first,name="first"),
     path("members/",views.members,name="members"),
     path("Workgroup/",views.workgroup,name="workgroup"),
      path('workgroup/data/', views.workgroup_data, name='workgroup_data'),
     path('login/discord/', views.login_with_discord, name='login_with_discord'),
    path('discord_callback/', views.discord_callback, name='discord_callback'),
       path('register/',views.register,name ='register'),
              path('profil/',views.profil,name ='profil'),



      
    ]