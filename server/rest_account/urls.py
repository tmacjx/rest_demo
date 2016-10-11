from django.conf.urls import include, url
from api import Login, UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserViewSet, base_name='users')


urlpatterns = [
    url(r'^login$', Login.as_view(), name='login'),

    url(r'^', include(router.urls)),
    # 用户 》》》 购物车 》》》商品

]

 # user
 # user/123
 # user/123/cart
 # user/123/cart/1

