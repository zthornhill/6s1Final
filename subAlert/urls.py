from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from api import views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # new
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', views.RegisterApi.as_view()),
    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),
    path('', views.subscription_list),
    url(r'^api/subscriptions/$', views.subscription_list),
    url(r'^api/subscriptions/(?P<pk>[0-9]+)$', views.getSubscription),
]
