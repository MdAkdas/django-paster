# Generated by Django 2.2.1 on 2019-05-26 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pasteapp', '0006_remove_paste_encrypted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pastes', to='accounts.User'),
        ),
    ]
