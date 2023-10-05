from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name = "index"),
    path('requestService', views.requestService, name = "requestService"),
    path('services', views.services, name = "services"),
    path('about', views.about, name = "about"),
    path('news', views.news, name = "news"),
    path('elements', views.elements, name = "elements"),
    path('userview', views.userview, name = "userview"),
    path('contact', views.contact, name = "contact"),
    path('message', views.message, name = "message"),
    path('innovation', views.innovation, name = "innovation"),
    path('projecthub', views.projecthub, name = "projecthub"),
    path('billing', views.billing, name = "billing"),
    path('projectorder', views.projectorder, name = "projectorder"),
    path('uploadfile', views.uploadfile, name = "uploadfile"),
    path('innovation', views.innovation, name = "innovation"),
    path('uploadproject', views.uploadproject, name = "uploadproject"),
    path('uploadtutorial', views.uploadtutorial, name = "uploadtutorial"),
    path('registereduser', views.registereduser, name = "registereduser"),
    
    
    path('viewmessage/<int:id>/', views.viewmessage, name = "viewmessage"),
    path('deletemessage/<int:id>/', views.deletemessage, name = "deletemessage"),
    path('viewservice/<int:id>/', views.viewservice, name = "viewservice"),
    path('deleteservice/<int:id>/', views.deleteservice, name = "deleteservice"),
    path('updateservice/<int:id>/', views.updateservice, name = "updateservice"),
    path('deleteprojectorder/<int:id>/', views.deleteprojectorder, name = "deleteprojectorder"),
    path('viewprojectorder/<int:id>/', views.viewprojectorder, name = "viewprojectorder"),
    
    
    path('signup', views.signup, name = "signup"),
    path('signin', views.signin, name = "signin"),
    path('logout', views.logout, name = "logout"),
    
    path('base', views.base, name = "base"),
    path('dashboard', views.dashboard, name = "dashboard"),
    path('tables', views.tables, name = "tables"),
    path('admin1', views.admin1, name = "admin1"),
    

]
