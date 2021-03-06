# Generated by Django 3.2.2 on 2021-05-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('title',), 'verbose_name': 'Blog', 'verbose_name_plural': 'Blog'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AddIndex(
            model_name='blog',
            index=models.Index(fields=['title'], name='blog_title_774334_idx'),
        ),
        migrations.AlterModelTable(
            name='blog',
            table='blog',
        ),
    ]
