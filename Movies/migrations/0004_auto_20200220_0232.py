# Generated by Django 3.0.2 on 2020-02-20 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0003_auto_20200220_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_info',
            name='preview_photo',
            field=models.CharField(max_length=150),
        ),
    ]