from django.urls import path,include
from . import views


urlpatterns=[
    path("Signout/", views.Signout, name="Signout"),
    path("", views.login, name="login"),
    path("first/",views.first,name="first"),
     path("members/",views.members,name="members"),
     path("Workgroup/",views.workgroup,name="workgroup"),
      path('workgroup/data/', views.workgroup_data, name='workgroup_data'),
     path('login/discord/', views.login_with_discord, name='login_with_discord'),
    path('callback/', views.discord_callback, name='discord_callback'),
       
    ]