from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from django.utils.translation import ugettext_lazy as _
from articles.models import Article



#Article Admin Starts Here
class ArticleResource(resources.ModelResource):
    title = fields.Field(column_name=_('Article Title'), attribute='title')
    description = fields.Field(column_name=_('Description'), attribute='description')
    tags = fields.Field(column_name=_('Tags'), attribute='tags')
    title_images = fields.Field(column_name=_('title_images'), attribute='title_images')
    external_links = fields.Field(column_name=_('external_links'), attribute='external_links')
    avg_read_time = fields.Field(column_name=_('avg_read_time'), attribute='avg_read_time')
    quality = fields.Field(column_name=_('quality'), attribute='quality')
    created_by = fields.Field(column_name=_('created_by'), attribute='created_by')
    created_date = fields.Field(column_name=_('created_date'), attribute='created_date')
    updated_by = fields.Field(column_name=_('updated_by'), attribute='updated_by')
    updated_date = fields.Field(column_name=_('updated_date'), attribute='updated_date')
    
    class Meta:
        model = Article
        fields = ('title','description','tags','title_images','external_links','avg_read_time','quality',
        'created_by','created_date','updated_by','updated_date')
        import_id_fields = fields
        export_order = fields
    
class ArticleAdmin(ImportExportModelAdmin):
    resource_class = ArticleResource
    list_display = ('title','short_description','external_links','avg_read_time','quality',)
    search_fields = ('title','external_links','quality',)
    list_filter = ('title','external_links','quality',)
#Article Admin Ends Here

# Register your models here.
admin.site.register(Article, ArticleAdmin)
