# coding=utf-8
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
# 根据request.method，自动调用对应的handler,比如get请求，自动去调用get()方法
# 常用的有.get(), .post(), put(), patch() and .delete().
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from rest_framework.generics import ListAPIView

from models import User
from serializers import LoginSerializer, UserSerializer

from rest_framework.decorators import detail_route, list_route


class CartView(APIView):
    # 继承自APIView(定义了框架级别默认的一些属性）
    # 单个view可以覆盖

    # get(), post(), put(), patch(), delete().
    # 序列化 python object -> json？html？
    renderer_classes = (JSONRenderer,)
    # 反序列化 默认json -> python object?
    parser_classes = (JSONParser,)
    # 权限
    permission_classes = (IsAuthenticated,)
    # 认证
    authentication_classes = (SessionAuthentication,)

    def get(self, request, pk):
        pass

    def post(self, request, pk):
        pass

    def put(self, request):
        pass

    def patch(self, request):
        pass

    def delete(self, request, pk):
        pass

# rest_framework.generics 生成视图


class Login(ListAPIView):
    queryset = User.object.all()
    authentication_classes = (BasicAuthentication,)
    serializer_class = LoginSerializer

    def get_queryset(self):
        queryset = super(Login, self).get_queryset()
        return queryset.filter(pk=self.request.user.pk)


# 将关联性强的view合并到一个viewsets中


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

    # 对应的url为 ^users/{pk}/me/$
    @detail_route()
    def me(self):
        pass

    # 对应的url为 ^users/nearby/$
    @list_route()
    def nearby(self):
        pass


class GoodsViewSet(viewsets.ModelViewSet):
    pass








