# Generated by Django 4.2.5 on 2023-09-19 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_computer_case_alter_computer_display_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='is_laptop',
            field=models.BooleanField(default=True),
        ),
    ]
