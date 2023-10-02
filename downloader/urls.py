from django.urls import path, include
from . import views
#from . import HodViews, StaffViews, StudentViews

urlpatterns = [
    path('', views.home_download, name="home_download"),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('download/', views.download, name="download")
    path('download/', views.download, name="download")
    #path('doLogin/', views.doLogin, name="doLogin"),
    #path('get_user_details/', views.get_user_details, name="get_user_details"),
]