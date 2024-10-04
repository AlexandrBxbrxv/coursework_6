# Generated by Django 4.2.2 on 2024-10-04 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailings', '0006_alter_mailing_options_alter_mailingtry_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailingtry',
            options={'ordering': ('name', 'last_try'), 'verbose_name': 'попытка рассылки', 'verbose_name_plural': 'попытки рассылки'},
        ),
        migrations.RemoveField(
            model_name='mailingtry',
            name='try_count',
        ),
        migrations.RemoveField(
            model_name='mailingtry',
            name='try_number',
        ),
        migrations.AddField(
            model_name='client',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_owner', to=settings.AUTH_USER_MODEL, verbose_name='владелец'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mailing_owner', to=settings.AUTH_USER_MODEL, verbose_name='владелец'),
        ),
        migrations.AddField(
            model_name='mailingtry',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='наименование'),
        ),
        migrations.AddField(
            model_name='mailingtry',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mailingtry_owner', to=settings.AUTH_USER_MODEL, verbose_name='владелец'),
        ),
        migrations.AddField(
            model_name='message',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='message_owner', to=settings.AUTH_USER_MODEL, verbose_name='владелец'),
        ),
    ]
