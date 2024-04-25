# Generated by Django 4.1.7 on 2023-03-23 22:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Belonging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Popular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('stars', models.IntegerField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='product')),
                ('location', models.TextField(blank=True, null=True)),
                ('create_At', models.DateField(auto_now_add=True)),
                ('update_At', models.DateField(default=datetime.date(9999, 12, 31))),
                ('type_id', models.IntegerField(blank=True, default=1, null=True)),
            ],
            options={
                'ordering': ['-create_At'],
            },
        ),
        migrations.CreateModel(
            name='Recommended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('stars', models.IntegerField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='product')),
                ('location', models.TextField(blank=True, null=True)),
                ('create_At', models.DateField(auto_now_add=True)),
                ('update_At', models.DateField(default=datetime.date(9999, 12, 31))),
                ('type_id', models.IntegerField(blank=True, default=2, null=True)),
            ],
            options={
                'ordering': ['-create_At'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=300, null=True)),
                ('address', models.CharField(blank=True, max_length=1024, null=True)),
                ('tombon', models.CharField(blank=True, max_length=1024, null=True)),
                ('amphure', models.CharField(blank=True, max_length=1024, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=12, null=True, verbose_name='ZIP')),
                ('province', models.CharField(blank=True, max_length=1024, null=True)),
                ('city', models.CharField(default='Thailand', max_length=1024)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Borrowed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('returned', models.DateTimeField(blank=True, null=True)),
                ('to_who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerceapp.friend')),
                ('what', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerceapp.belonging')),
            ],
        ),
    ]
