# Generated by Django 4.2.2 on 2023-06-26 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_remove_profile_email_profile_name_profile_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
