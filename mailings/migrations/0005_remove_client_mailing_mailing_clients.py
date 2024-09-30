# Generated by Django 4.2.2 on 2024-09-30 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0004_mailingtry_mailing_mailing_try'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='mailing',
        ),
        migrations.AddField(
            model_name='mailing',
            name='clients',
            field=models.ManyToManyField(related_name='mailing_clients', to='mailings.client', verbose_name='клиенты рассылки'),
        ),
    ]
