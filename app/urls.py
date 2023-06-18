from django.contrib import admin
from django.urls import path,include

from app import views
urlpatterns = [
    path('login',views.login,name="login"),
    path('',views.home,name="home"),
    path('mess',views.mess,name="mess"),
    path('logout',views.logout,name="logout"),
    path('change',views.change,name="change"),
    path('respond',views.respond,name="respond"),
    path('pers',views.pers,name="pers"),
    path('lib',views.lib,name="lib"),
    path('sub',views.sub,name="sub"),
    path('teach',views.teach,name="teach"),
    path('mst',views.mst,name="mst"),
    path('est',views.est,name="est"),
    path('sessional',views.sessional,name="sessional"),
    path('grades',views.grades,name="grades"),
    path('hostelaaloc',views.hostelalloc,name="hostelalloc"),
]