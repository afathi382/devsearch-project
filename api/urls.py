from django.urls import path, include
from . import views  

# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r'profiles', views.ProfileViewSet)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.gettest),
    path('projects/', views.getprojects),
    path('projects/<str:pk>', views.getproject),
    path('profiles/', views.getprofiles),
    path('profiles/<str:pk>', views.getprofile),

    path('create-project', views.createproject),
    
    
]


