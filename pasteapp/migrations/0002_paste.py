# Generated by Django 2.2.1 on 2019-05-23 08:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190523_1145'),
        ('pasteapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('syntax', models.CharField(max_length=20)),
                ('expire_time', models.DateTimeField(blank=True, default=None)),
                ('expire', models.CharField(blank=True, max_length=20)),
                ('status', models.BooleanField(default=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('self_destroy', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.User')),
            ],
        ),
    ]
