# Generated by Django 4.0 on 2022-02-21 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_management', '0002_alter_member_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='surname',
            field=models.CharField(max_length=50),
        ),
    ]
