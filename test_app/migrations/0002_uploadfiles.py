# Generated by Django 3.1.6 on 2021-02-19 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('image_file', models.ImageField(upload_to='images/')),
            ],
        ),
    ]