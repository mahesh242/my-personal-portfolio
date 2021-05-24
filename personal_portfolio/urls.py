"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = i18n_patterns(
    url('rusty_codes_admin/', admin.site.urls),
    url('', include('home.urls')),
    url('my_portfolio/', include('portfolio.urls')),
    url('user_profile/', include('user_profile.urls')),
    url('blog/', include('blog.urls')),
    url('articles/', include('articles.urls')),
    url('my_todo/', include('todo.urls')),
    url('master_data/', include('master.urls')),
    url('videos/', include('videos.urls')),
    url(r'^api/', include(('rest_api.urls', 'rest_api'), namespace='rest_api')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Debug Toolbar If DEBUG TRUE in Settings.py
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         url('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns

# Change admin site title
admin.site.site_header = 'Portfolio Admin'
admin.site.site_title = 'Portfolio Admin'
admin.site.index_title = 'Portfolio Administration'

