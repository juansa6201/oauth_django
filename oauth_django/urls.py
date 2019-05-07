from django.urls import include, path
from rest_framework import routers
from . import views
from oauth_django.views import index
from oauth_django.views import logout_view

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('logout/', logout_view, name='logout'),
    path('api/', include(router.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

]