# Generated by Django 2.1.7 on 2019-03-14 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
