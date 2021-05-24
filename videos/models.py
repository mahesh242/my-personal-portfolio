from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.translation import ugettext_lazy as _
from audit_log.models.fields import CreatingUserField, LastUserField
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField
from master.models import VideoMaster


class Videos(models.Model):
    class Quality(models.IntegerChoices):
        DIAMOND = 1
        SPADE = 2
        HEART = 3
        CLUB = 4

    video_category =  models.ForeignKey(VideoMaster,  on_delete=models.CASCADE, verbose_name=_("Article Category"))
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    video_url = models.URLField(max_length=200, blank=True, null=True,verbose_name=_("Video URL"))
    video_playlist_id = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Video Play list ID"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    tags = models.CharField(max_length=250, blank=True, null=True, verbose_name=_("Tags"))
    title_images = models.ImageField(upload_to='Article/Images/', verbose_name=_("Title Images"))
    quality = models.IntegerField(choices=Quality.choices, blank=True, null=True, verbose_name=_("Quality"))
    created_by = CreatingUserField(related_name = "VideosCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "VideosUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 50)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Videos"
        verbose_name_plural = "Videos"
        db_table = 'videos'
        ordering=('title',)
        indexes = [
                models.Index(fields=['title'])
            ]
        