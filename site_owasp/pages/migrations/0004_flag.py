# Generated by Django 2.2.5 on 2020-01-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200123_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_faille', models.IntegerField()),
                ('flag', models.CharField(max_length=50)),
            ],
        ),
    ]