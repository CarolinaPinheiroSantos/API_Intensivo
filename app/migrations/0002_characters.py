# Generated by Django 5.1.4 on 2025-01-10 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Characters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('vampire', models.BooleanField()),
                ('eyesColor', models.CharField(max_length=100)),
                ('hairColor', models.CharField(max_length=100)),
                ('actor', models.CharField(max_length=100)),
                ('imagem', models.TextField()),
            ],
        ),
    ]
