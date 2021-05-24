from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from master import views as master_views
from master.views import StateAutocomplete, CityAutocomplete

app_name = "master"

urlpatterns = [
    url(r'^state-autocomplete/$',StateAutocomplete.as_view(),name='state-autocomplete',),
    url(r'^city-autocomplete/$',CityAutocomplete.as_view(),name='city-autocomplete',),

]