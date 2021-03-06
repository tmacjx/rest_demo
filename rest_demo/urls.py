"""rest_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
from views import index, trya, tryj
from django.conf import settings
from django.conf.urls.static import static

api_v1 = [

    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # url(r'', include('BHU.rest_user.urls'))
    # url(r'', include('account.urls')),

    url(r'', include('server.rest_account.urls')),

]


urlpatterns = [
    url(r'^admin/', admin.site.urls),


    url(r'^index/$', index, name='index'),

    url(r'^Test1/$', tryj, name='test1'),

    url(r'^Test2/$', trya, name='test2'),

    url(r'^api/v1/', include(api_v1)),
]
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns = patterns('',
#                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#                                {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#                            url(r'', include(
#                                'django.contrib.staticfiles.urls')),
#                            ) + urlpatterns