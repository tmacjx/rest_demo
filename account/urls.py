from django.conf.urls import url, include
from rest_framework import routers
from account import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, base_name='users')


urlpatterns = [
    url(r'^', include(router.urls)),

    # url(r'^')




]
