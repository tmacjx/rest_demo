# coding=utf-8
from django.conf.urls import include, url
from api import Login, UserViewSet, ProductViewSet, SignUp, UserListViewList, ProductAdminViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserViewSet, base_name='users')
router.register('users', UserListViewList, base_name='users_list')

router.register('products', ProductViewSet, base_name='products')
router.register('products', ProductAdminViewSet, base_name='products_admin')

urlpatterns = [
    url(r'^', include(router.urls)),


    url(r'^login/$', Login.as_view(), name='login'),
    # url(r'^signin/$', SignIn.as_view(), name='sign'),
    url(r'^signup/$', SignUp.as_view(), name='signup'),

]

# 查看所有的user, 权限为admin
# users/

# user信息
# cart

# 单个user
# users/pk／
# user信息
# cart

# 单个user下的cart
# users/pk/cart
# cart信息


# products/pk/
# 产品信息