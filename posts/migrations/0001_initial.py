# Generated by Django 2.1.1 on 2018-09-17 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('site_url', models.TextField(default='')),
                ('content', models.TextField(default='')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('votes_total', models.IntegerField(default=1)),
                ('image', models.ImageField(default='', upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
