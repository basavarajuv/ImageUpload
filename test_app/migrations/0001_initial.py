# Generated by Django 3.1.6 on 2021-02-16 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModelName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
