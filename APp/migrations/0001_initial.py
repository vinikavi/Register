# Generated by Django 2.2.4 on 2019-08-22 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=20)),
                ('cno', models.IntegerField()),
            ],
        ),
    ]
