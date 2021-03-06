# Generated by Django 3.2.7 on 2021-09-25 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAlerts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=256, verbose_name='Email')),
                ('period', models.IntegerField(choices=[('2', '2 minutes'), ('10', '10 minutes'), ('20', '20 minutes')], default=20, verbose_name='Period')),
                ('search_phrase', models.CharField(max_length=256, verbose_name='Search Phrase')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
            ],
            options={
                'verbose_name': 'User Alert',
                'verbose_name_plural': 'User Alerts',
            },
        ),
        migrations.CreateModel(
            name='EbayItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=250, unique=True, verbose_name='Item ID')),
                ('title', models.CharField(max_length=1000, verbose_name='Title')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='Short Description')),
                ('category_path', models.CharField(max_length=250, verbose_name='Item ID')),
                ('image_url', models.URLField(max_length=250, verbose_name='Image URL')),
                ('item_web_url', models.URLField(max_length=250, verbose_name='Item URL')),
                ('description', models.TextField(verbose_name='Description')),
                ('category_id', models.CharField(max_length=250, verbose_name='Category ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('value', models.DecimalField(decimal_places=3, default=0.0, max_digits=6, verbose_name='Value')),
                ('currency', models.CharField(max_length=10, verbose_name='Currency')),
                ('user_alert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_alerts.useralerts', verbose_name='User Alert')),
            ],
            options={
                'verbose_name': 'eBay Card Item',
                'verbose_name_plural': 'eBay Card Items',
            },
        ),
    ]
