# Generated by Django 4.1.7 on 2023-03-11 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mriic',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=30)),
                ('emp_age', models.CharField(max_length=30)),
            ],
        ),
    ]
