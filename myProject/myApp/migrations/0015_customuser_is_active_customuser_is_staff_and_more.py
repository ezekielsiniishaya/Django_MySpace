# Generated by Django 5.1.3 on 2024-11-17 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0014_customuser_about_customuser_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='password',
            field=models.CharField(default='password', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
