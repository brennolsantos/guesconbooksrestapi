# Generated by Django 3.2.9 on 2021-12-01 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_company_update_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Price'),
        ),
    ]
