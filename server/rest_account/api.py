# coding=utf-8
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

from serializers import LoginSerializer, UserSerializer, SignUpSerializer, CartSerializer, ProductSerializer, \
    SignInSerializer

from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import IsAdminUser, AllowAny
from models import Product, Cart
from rest_framework import status
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from viewSet import AlterModelViewSet
from permissions import IsAdminOrReadOnly
from django.contrib.auth import get_user_model, authenticate, login
from rest_framework_extensions.mixins import NestedViewSetMixin
from models import Cart
from rest_framework.exceptions import AuthenticationFailed
User = get_user_model()


# 用作API测试登陆用
class Login(ListAPIView):
    queryset = User.objects.all()
    authentication_classes = (BasicAuthentication,)
    serializer_class = LoginSerializer

    def get_queryset(self):
        queryset = super(Login, self).get_queryset()
        return queryset.filter(pk=self.request.user.pk)


class SignIn(APIView):
    """
    Same function as `Login` but doesn't use basic auth. This is for web clients,
    so we don't see a browser popup for basic auth.
    """
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        if 'username' not in request.data:
            msg = 'Username required'
            raise AuthenticationFailed(msg)
        elif 'password' not in request.data:
            msg = 'Password required'
            raise AuthenticationFailed(msg)

        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is None or not user.is_active:
            raise AuthenticationFailed('Invalid username or password')
        # 设置cookie
        login(request, user)
        serializer = SignInSerializer(instance=user)
        return Response(serializer.data, status=200)


# 注册
class SignUp(CreateAPIView):
    serializer_class = SignUpSerializer


class UserListViewList(viewsets.ViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)

    def list(self, request):
        serializer = UserSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = super(UserViewSet, self).get_queryset()
        return queryset.filter(pk=self.request.user.pk)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.pop('pk', self.request.user.pk)
        instance = User.objects.get(pk=pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = User.objects.get(pk=self.request.user.pk)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, pk=None):
        instance = self.get_queryset()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 对应的url为 ^users/me/$
    @list_route()
    def me(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # 对应的url为 ^users/{pk}/cart/$
    @detail_route()
    def cart(self, request, pk=None):
        user = User.objects.get(pk=pk)
        queryset = Cart.objects.get(user=user)
        serializer = CartSerializer(queryset)
        return Response(serializer.data)


# 默认用户 无需auth                list retrieve
# 管理员 需要auth  permisson控制   create() update() partial_update()  destroy()
class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    authentication_classes = (SessionAuthentication, BasicAuthentication)


class CartViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer












