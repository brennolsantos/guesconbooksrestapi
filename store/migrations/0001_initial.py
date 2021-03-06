# Generated by Django 3.2.9 on 2021-11-17 23:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=100, verbose_name='Last Name')),
                ('desc', models.TextField(blank=True, max_length=1200, verbose_name='Desc')),
                ('birth_date', models.DateField(blank=True, verbose_name='Birth')),
                ('picture', models.ImageField(null=True, upload_to='authors/', verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Basket',
                'verbose_name_plural': 'Baskets',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, unique=True, verbose_name='Name')),
                ('desc', models.TextField(blank=True, max_length=1200, verbose_name='Desc')),
                ('picture', models.ImageField(null=True, upload_to='companies/', verbose_name='Photo')),
                ('creat_date', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('update_date', models.DateField(blank=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Companie',
                'verbose_name_plural': 'Companies',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, unique=True, verbose_name='Genre')),
                ('desc', models.TextField(blank=True, max_length=1200, verbose_name='Desc')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax', models.DecimalField(blank=True, decimal_places=2, max_digits=4, verbose_name='Discount')),
                ('start', models.DateTimeField(auto_now_add=True, verbose_name='Start date')),
                ('finish', models.DateTimeField(verbose_name='Finish')),
            ],
            options={
                'verbose_name': 'Promo',
                'verbose_name_plural': 'Promos',
                'ordering': ['start'],
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Title')),
                ('edition', models.PositiveSmallIntegerField(null=True, verbose_name='Edition')),
                ('desc', models.TextField(blank=True, max_length=1200, verbose_name='Desc')),
                ('num_pages', models.PositiveIntegerField(null=True, verbose_name='Number of pages')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Price')),
                ('cover', models.ImageField(null=True, upload_to='magazine', verbose_name='Cover')),
                ('publish_date', models.DateTimeField(null=True, verbose_name='Published')),
                ('creat_date', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.company')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.genre')),
            ],
            options={
                'verbose_name': 'Magazine',
                'verbose_name_plural': 'Magazines',
                'ordering': ['title', '-edition'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Title')),
                ('desc', models.TextField(blank=True, max_length=1200, verbose_name='Desc')),
                ('num_pages', models.PositiveIntegerField(null=True, verbose_name='Number of Pages')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Price')),
                ('cover', models.ImageField(null=True, upload_to='books/', verbose_name='Cover')),
                ('publish_date', models.DateTimeField(null=True, verbose_name='Published')),
                ('creat_date', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.author')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.company')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.genre')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['title', 'author'],
            },
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_pk', models.PositiveBigIntegerField(verbose_name='Item ID')),
                ('item_type', models.CharField(blank=True, max_length=100, verbose_name='Type')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.basket')),
            ],
            options={
                'verbose_name': 'BItem',
                'verbose_name_plural': 'BItems',
            },
        ),
        migrations.AddField(
            model_name='basket',
            name='promo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.promo'),
        ),
        migrations.AddField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
