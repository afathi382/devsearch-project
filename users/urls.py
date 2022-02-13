from django.urls import path
from . import views  

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.profiles , name='profiles'),
    path('login-user/', views.loginUser , name='loginUser'),
    path('logout-user/', views.logoutUser , name='logoutUser'),
    path('registration-user/', views.registrationUser , name='registrationUser'),
    path('user-profile/<str:pk>', views.userProfile , name='userProfile'),
    path('account/', views.account , name='account'),
    path('editaccount/', views.editaccount , name='editaccount'),
    path('user-profile/create-message/<str:pk>', views.create_message , name='create-message'),
    path('inbox/', views.inbox , name='inbox'),
    path('inbox/single-message/<str:pk>', views.single_message , name='single-message'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

