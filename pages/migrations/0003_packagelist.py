# Generated by Django 4.2.3 on 2023-07-27 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_contactlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='packageList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pkgName', models.CharField(max_length=100)),
                ('pkgMprice', models.IntegerField()),
                ('pkgBprice', models.IntegerField()),
                ('pkgDisc', models.TextField(max_length=100)),
            ],
        ),
    ]