# Generated by Django 3.2 on 2022-01-16 13:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pipeline_name', models.CharField(max_length=30, unique=True)),
                ('pipeline_des', models.CharField(blank=True, max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('interval', models.CharField(choices=[('1d', 'Daily'), ('7d', 'Weekly'), ('14d', 'Bi-weekly'), ('30d', 'Monthly'), ('60d', 'Bi-monthly')], default=None, max_length=15)),
                ('output_image', models.CharField(choices=[('a8fc3dde-a3e8-11e7-9793-ae4260ee3b4b', 'True Colour'), ('1f0db8b2-b4d4-11e7-a775-a6fe70ce62b1', 'False Colour Urban'), ('154311a8-582a-11e7-b30d-7291b81e23e3', 'False Colour Infrared'), ('c31c1bea-a4be-11e7-8650-3ae5c7149ea7', 'All Optical Bands'), ('3cab2e68-b4d4-11e7-a775-a6fe70ce62b1', 'MSAVI2'), ('ga23d8a2-8f3d-481c-b7ef-9fa02839aab0', 'Near-infrared')], max_length=100)),
                ('aoi', models.JSONField(null=True)),
                ('cloud_cover', models.CharField(max_length=10)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('aoi_area', models.CharField(max_length=10)),
                ('created_by', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=30)),
                ('api_id', models.CharField(max_length=100)),
                ('num_results', models.PositiveIntegerField()),
                ('num_images', models.PositiveIntegerField()),
                ('results_updated', models.DateTimeField()),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
