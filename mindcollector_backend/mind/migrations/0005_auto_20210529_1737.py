# Generated by Django 2.2.7 on 2021-05-29 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mind', '0004_auto_20210529_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eintrag',
            name='AUDIO',
            field=models.TextField(blank=True, default=''),
        ),
    ]
