from django.urls import path, include
from . import views
#from . import HodViews, StaffViews, StudentViews

urlpatterns = [
    path('', views.home_download, name="home_download"),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('download/', views.download, name="download"),
    path('home/', views.home_download, name="home"),
    path('blogs/', views.blogs, name="blogs"),
    path('about/', views.about, name="about"),
    path('contactus/', views.contactus, name="contactus"),
    #path('doLogin/', views.doLogin, name="doLogin"),
    #path('get_user_details/', views.get_user_details, name="get_user_details"),
]