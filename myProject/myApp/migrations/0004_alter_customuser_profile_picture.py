# Generated by Django 5.1.3 on 2024-11-16 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_alter_customuser_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', upload_to='media/profile_pics/'),
        ),
    ]
