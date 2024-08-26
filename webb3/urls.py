from django.urls import path,include
from . import views


urlpatterns=[
    path("Signout/", views.Signout, name="Signout"),
    path("", views.login, name="login"),
    path("first/",views.first,name="first"),
     path("Members/",views.members,name="members"),
     path("Workgroup/",views.workgroup,name="workgroup"),
      path('workgroup/data/', views.workgroup_data, name='workgroup_data'),
       path('login/github/', views.login_with_github, name='login_with_github'),
    path('callback/',views.github_callback, name='github_callback'),
       
    ]