# Generated by Django 3.2.9 on 2021-12-01 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_genre_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='update_date',
            field=models.DateField(blank=True, null=True, verbose_name='Updated'),
        ),
    ]
