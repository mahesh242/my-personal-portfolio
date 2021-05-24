from django.db import models
from django.contrib.auth.models import User, Group
from django.template.defaultfilters import truncatechars
from django.utils.translation import ugettext_lazy as _
from master.models import StateMaster, CityMaster

class UserDetails(models.Model):
    Profile_dis_CHOICE = ( 
        (u'0', u'No'),
        (u'1', u'Opt for Disable'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    profile_photo = models.ImageField(upload_to='Profile_Image/', default='', blank=True, null=True, verbose_name="Profile Photo")
    mobile_no = models.BigIntegerField(verbose_name=_("Mobile Number"))
    additional_mobile_no = models.BigIntegerField(blank=True, null=True, verbose_name=_("Additional Mobile Number"))
    
    address_line_1 = models.TextField(blank=True, null=True,verbose_name=_("Address Line 1")) 
    address_line_2 = models.TextField(blank=True, null=True,verbose_name=_("Address Line 2"))
    pincode = models.BigIntegerField(blank=True, null=True,  verbose_name=_("Pin Code"))
    state =  models.ForeignKey(StateMaster, blank=True, null=True, on_delete=models.CASCADE, verbose_name=_("State"))
    city =  models.ForeignKey(CityMaster,  blank=True, null=True, on_delete=models.CASCADE, verbose_name=_("City"))
 
    profile_approved_datetime = models.DateTimeField(blank=True, null=True, verbose_name=("Profile Approved Date Time"))
    profile_approved_remarks = models.TextField(blank=True, null=True,verbose_name=_("Profile Approved Remarks")) 
    profile_dis_opt_by_status = models.CharField(max_length=1, default='0',choices=Profile_dis_CHOICE, verbose_name=_("Profile Disabled Opt By Status"))
    profile_dis_opt_by_remarks =  models.TextField(blank=True, null=True,verbose_name=_("Profile Disabled Opt By Remarks")) 
    profile_dis_opt_by_datetime = models.DateTimeField(blank=True, null=True, verbose_name=(" Profile Disabled Opt By Date Time"))
    profile_dis_by_remarks = models.TextField(blank=True, null=True,verbose_name=_("Profile Disabled By Remarks")) 
    profile_dis_by_datetime =  models.DateTimeField(blank=True, null=True, verbose_name=(" Profile Disabled By Date Time"))
    profile_approved_by =  models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name=_("Profile Approved By"), related_name = "ProfileApprovedBy")
    profile_dis_by= models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name=_("Profile Disabled By"), related_name = "ProfiledisBy")
    profile_status = models.CharField(max_length=100, blank=True, null=True, verbose_name=_(" Profile Status"))
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "UserDetails"
        verbose_name_plural = "UserDetails"
        db_table = 'user_details'
        indexes = [
                models.Index(fields=['user'])
            ]
        