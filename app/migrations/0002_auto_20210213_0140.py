# Generated by Django 3.1.6 on 2021-02-13 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='pics/'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='pics/'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='img4',
            field=models.ImageField(blank=True, null=True, upload_to='pics/'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='img5',
            field=models.ImageField(blank=True, null=True, upload_to='pics/'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='img6',
            field=models.ImageField(blank=True, null=True, upload_to='pics/'),
        ),
    ]
