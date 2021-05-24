from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget, DateTimeWidget, IntegerWidget
from import_export.admin import ImportMixin, ExportMixin, ImportExportMixin
from import_export.formats import base_formats
from import_export import resources, fields
from django.forms import forms, ModelForm, Select
from master.models import ArticlesMaster,CityMaster,StateMaster,Tags,VideoMaster

#State Admin Starts Here
class StateMasterResource(resources.ModelResource):
    state_name = fields.Field(column_name=_('State Name'), attribute='state_name')
    country_id = fields.Field(column_name=_('Country Id'), attribute='country_id',)
    
    class Meta:
        model = StateMaster
        fields = ('state_name','country_id', )
        import_id_fields = fields
        export_order = fields
    
class StateMasterAdmin(ImportExportModelAdmin):
    resource_class = StateMasterResource
    list_display = ('state_name','country_id', )
    search_fields = ('state_name',)
#State Admin Ends Here

#City Admin Starts Here
class CityMasterResource(resources.ModelResource):
    city_name = fields.Field(column_name=_('City Name'), attribute='city_name')
    state = fields.Field(column_name=_('State Name'), attribute='state', widget=ForeignKeyWidget(StateMaster, 'state_name'))
    
    class Meta:
        model = CityMaster
        fields = ('city_name', 'state',)
        import_id_fields = fields
        export_order = fields
    
class CityMasterAdmin(ImportExportModelAdmin):
    resource_class = CityMasterResource
    list_display = ('city_name','state', )
    search_fields = ('city_name','state__state_name',)
    list_filter = ('state',)
#City Admin End Here

# Register your models here.
admin.site.register(ArticlesMaster)
admin.site.register(VideoMaster)
admin.site.register(Tags)
admin.site.register(StateMaster, StateMasterAdmin)
admin.site.register(CityMaster, CityMasterAdmin)