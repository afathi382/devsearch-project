# Generated by Django 3.2.8 on 2021-10-28 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20211028_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='vot_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='vot_total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
