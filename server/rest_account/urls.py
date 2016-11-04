# coding=utf-8
from django.conf.urls import include, url
from api import Login, UserViewSet, ProductViewSet, SignUp, UserListViewList, CartViewSet, SignIn
from rest_framework import routers
from rest_framework_extensions.mixins import DetailSerializerMixin
from rest_framework_extensions.routers import ExtendedSimpleRouter, ExtendedDefaultRouter


#
# router = routers.DefaultRouter()
# # router = routers.SimpleRouter()
#
# router.register('users', UserViewSet)
# router.register('users', UserListViewList)
#
# router.register('products', ProductViewSet)
# # router.register('products', ProductAdminViewSet)
router = ExtendedDefaultRouter()
(
    router.register(r'users', UserListViewList, base_name='users')
          .register(r'carts', CartViewSet, base_name='carts', parents_query_lookups=['user'])
)

router2 = routers.DefaultRouter()

router2.register('products', ProductViewSet)


urlpatterns = [
    url(r'', include(router.urls)),

    url(r'', include(router2.urls)),

    url(r'login/$', Login.as_view(), name='login'),
    # url(r'^signin/$', SignIn.as_view(), name='sign'),
    url(r'signup/$', SignUp.as_view(), name='signup'),

    url(r'signin/$', SignIn.as_view(), name='signin'),

]

