# Generated by Django 2.0.5 on 2018-09-16 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20180916_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
