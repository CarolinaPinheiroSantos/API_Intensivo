# Generated by Django 5.1.4 on 2025-01-10 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_house_characters_creaeted_characters_house'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='description',
            field=models.TextField(),
        ),
    ]