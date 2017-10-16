"""handifinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from bdat import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^categories/assistance$', views.categorya, name='assistance'),
    url(r'^categories/fonctions$', views.categoryf, name='fonctions'),
    url(r'^techno/([0-9]+)/$', views.technology, name='technology'),
    url(r'^search/(?:(?P<words>\w{0, 50})/)?$', views.search, name='search'),
    # url(r'^search/(?:(?P<words>\w{0,50})/)$', views.search, name='search'),
# r'^post/(?:(?P<slug>\w+)/)?save/'

]
