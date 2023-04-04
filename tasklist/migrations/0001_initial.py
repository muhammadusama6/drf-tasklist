# Generated by Django 4.1.7 on 2023-03-21 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tasklistModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField(default=0)),
                ('task_name', models.CharField(default='', max_length=100)),
                ('is_checked', models.BooleanField(default=False)),
            ],
        ),
    ]
