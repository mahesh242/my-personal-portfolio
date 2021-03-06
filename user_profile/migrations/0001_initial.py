# Generated by Django 3.2.2 on 2021-05-13 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0003_auto_20210513_2110'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, default='', null=True, upload_to='Profile_Image/', verbose_name='Profile Photo')),
                ('mobile_no', models.BigIntegerField(verbose_name='Mobile Number')),
                ('additional_mobile_no', models.BigIntegerField(blank=True, null=True, verbose_name='Additional Mobile Number')),
                ('address_line_1', models.TextField(blank=True, null=True, verbose_name='Address Line 1')),
                ('address_line_2', models.TextField(blank=True, null=True, verbose_name='Address Line 2')),
                ('pincode', models.BigIntegerField(blank=True, null=True, verbose_name='Pin Code')),
                ('profile_approved_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Profile Approved Date Time')),
                ('profile_approved_remarks', models.TextField(blank=True, null=True, verbose_name='Profile Approved Remarks')),
                ('profile_dis_opt_by_status', models.CharField(choices=[('0', 'No'), ('1', 'Opt for Disable')], default='0', max_length=1, verbose_name='Profile Disabled Opt By Status')),
                ('profile_dis_opt_by_remarks', models.TextField(blank=True, null=True, verbose_name='Profile Disabled Opt By Remarks')),
                ('profile_dis_opt_by_datetime', models.DateTimeField(blank=True, null=True, verbose_name=' Profile Disabled Opt By Date Time')),
                ('profile_dis_by_remarks', models.TextField(blank=True, null=True, verbose_name='Profile Disabled By Remarks')),
                ('profile_dis_by_datetime', models.DateTimeField(blank=True, null=True, verbose_name=' Profile Disabled By Date Time')),
                ('profile_status', models.CharField(blank=True, max_length=100, null=True, verbose_name=' Profile Status')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.citymaster', verbose_name='City')),
                ('profile_approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ProfileApprovedBy', to=settings.AUTH_USER_MODEL, verbose_name='Profile Approved By')),
                ('profile_dis_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ProfiledisBy', to=settings.AUTH_USER_MODEL, verbose_name='Profile Disabled By')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.statemaster', verbose_name='State')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'UserDetails',
                'verbose_name_plural': 'UserDetails',
                'db_table': 'user_details',
            },
        ),
        migrations.AddIndex(
            model_name='userdetails',
            index=models.Index(fields=['user'], name='user_detail_user_id_7bd0e0_idx'),
        ),
    ]
