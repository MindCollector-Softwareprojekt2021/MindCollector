# Generated by Django 2.2.7 on 2021-06-05 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mind', '0013_auto_20210605_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eintrag',
            name='CREATED_AT',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='kathegorie',
            name='CREATED_AT',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]