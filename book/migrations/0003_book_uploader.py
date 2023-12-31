# Generated by Django 4.2.2 on 2023-06-26 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_profile_profile_picture_user_profile_picture'),
        ('book', '0002_book_trending'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='uploader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_books', to='account.profile'),
        ),
    ]
