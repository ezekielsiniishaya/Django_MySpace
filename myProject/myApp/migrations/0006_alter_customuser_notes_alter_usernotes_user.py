# Generated by Django 5.1.3 on 2024-11-16 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='notes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UserNotes', to='myApp.usernotes'),
        ),
        migrations.AlterField(
            model_name='usernotes',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='CustomUser', to='myApp.customuser'),
        ),
    ]
