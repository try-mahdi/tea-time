# Generated by Django 4.1.7 on 2023-09-02 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='extras',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='sugar',
            field=models.IntegerField(null=True),
        ),
    ]
