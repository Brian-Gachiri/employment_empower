# Generated by Django 4.2.2 on 2023-06-14 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_clientmembership_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='interests',
            field=models.TextField(blank=True, null=True),
        ),
    ]