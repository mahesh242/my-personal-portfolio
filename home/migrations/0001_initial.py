# Generated by Django 3.2.2 on 2021-05-18 11:51

import audit_log.models.fields
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0005_videomaster'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('tags', models.CharField(blank=True, max_length=250, null=True, verbose_name='Tags')),
                ('title_images', models.ImageField(upload_to='Article/Images/', verbose_name='Title Images')),
                ('quality', models.IntegerField(blank=True, choices=[(1, 'Diamond'), (2, 'Spade'), (3, 'Heart'), (4, 'Club')], null=True, verbose_name='Quality')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', audit_log.models.fields.CreatingUserField(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='VideosCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('updated_by', audit_log.models.fields.LastUserField(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='VideosUpdatedBy', to=settings.AUTH_USER_MODEL)),
                ('video_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.videomaster', verbose_name='Article Category')),
            ],
            options={
                'verbose_name': 'Videos',
                'verbose_name_plural': 'Videos',
                'db_table': 'videos',
                'ordering': ('title',),
            },
        ),
        migrations.AddIndex(
            model_name='videos',
            index=models.Index(fields=['title'], name='videos_title_883151_idx'),
        ),
    ]