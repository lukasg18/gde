"""gde URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from app.views import *
from app import admin as adminMethod

urlpatterns = [
                  url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
                  url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
                  url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm, name='password_reset_confirm'),
                  url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
                  url(r'^admin/', admin.site.urls),
                  url(r'^register/$', cadastroUsuario, name='cadastro_usuario'),
                  url(r'^home/$', home),
                  url(r'^user/(?P<pk>[\d]+)/$', user_detail),
                  url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='login'),
                  url(r'^logout/$', auth_views.logout, {'next_page': '/'}),
                  url(r'^levantamento_list/$', levantamento_list, name='levantamento_list'),
                  url(r'^levantamento/(?P<pk>\d+)/edit/$', levantamento_edit, name='levantamento_edit'),
                  url(r'^tipologia/$', cadastrar_tipologia, name="cadastrar_tipologia"),
                  url(r'^levantamento/(?P<pk>\d+)/view/$', levantamento_view, name='levantamento_view'),
                  url(r'^tipologia/(?P<pk>\d+)/resposta/$', resposta_view, name='resposta_view'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

