from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.translation import ugettext_lazy as _
from audit_log.models.fields import CreatingUserField, LastUserField
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField


class ArticlesMaster(models.Model):
    Category= (
        (u'', u'Select'),
        (u'Dart', u'Dart'),
        (u'Django', u'Django'),
        (u'Flutter', u'Flutter'),
        (u'Python', u'Python'),
        (u'Linux', u'Linux'),
    )   
    category = models.CharField(max_length=25, choices=Category, verbose_name=_("Category"))
    description = models.CharField(max_length=250, verbose_name=_("Description"))
    created_by = CreatingUserField(related_name = "ArticlesMasterCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "ArticlesMasterUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 50)


    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "ArticlesMaster"
        verbose_name_plural = "ArticlesMaster"
        db_table = 'articles_master'
        ordering=('category',)
        indexes = [
                models.Index(fields=['category'])
            ]
        
class Tags(models.Model):
    tag_name = models.CharField(max_length=50, verbose_name=_("Tag Name"))
    related_to = models.CharField(max_length=50, verbose_name=_("Related"))

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = "Tags"
        verbose_name_plural = "Tags"
        db_table = 'tags'

# class ArticlesImages(models.Model):
#     image_name = models.CharField(max_length=50, verbose_name=_("Image Name"))
#     image = models.ImageField(upload_to='Article/Images/', height_field=None, width_field=None, max_length=100, verbose_name=_("Image"))
    
#     def __str__(self):
#         return self.image_name

#     class Meta:
#         verbose_name = "Images"
#         verbose_name_plural = "Images"
#         db_table = 'images'
        

#State Model Starts here
class StateMaster(models.Model):
    COUNTRY_CHOICES = (
        (u'1', u'INDIA'),
    )
    state_name = models.CharField(max_length=100, verbose_name=_("State Name"))
    country_id = models.CharField(max_length=1, default=1, choices=COUNTRY_CHOICES, verbose_name=_("Country Name"))
    created_by = CreatingUserField(related_name = "StateMasterCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "StateMasterUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.state_name
    
    class Meta:
        verbose_name = "State Master"
        verbose_name_plural = "State Master"
        db_table = 'state_master'
        ordering=('state_name',)
        indexes = [
                models.Index(fields=['state_name'])
            ]
#State Model Ends here

#City Model Starts here
class CityMaster(models.Model):
    state =  models.ForeignKey(StateMaster,  on_delete=models.CASCADE, verbose_name=_("State Name"))
    city_name = models.CharField(max_length=100, verbose_name=_("City Name"))
    created_by = CreatingUserField(related_name = "CityMasterCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CityMasterUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.city_name
    
    class Meta:
        verbose_name = "City Master"
        verbose_name_plural = "City Master"
        db_table = 'city_master'
        ordering=('city_name',)
        indexes = [
            models.Index(fields=['city_name'])
        ]

#City Model Ends here

#VideoMaster Model Starts here
class VideoMaster(models.Model):
    Video= (
        (u'', u'Select'),
        (u'Flutter', u'Flutter'),
        (u'Django', u'Django'),
        (u'Python', u'Python'),
        (u'Dart', u'Dart'),
    )   
    video_category = models.CharField(max_length=25, choices=Video, verbose_name=_("Video Category"))
    description = models.CharField(max_length=250, verbose_name=_("Description"))
    created_by = CreatingUserField(related_name = "VideoMasterCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "VideoMasterUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 50)


    def __str__(self):
        return self.video_category
#VideoMaster Model Ends here

