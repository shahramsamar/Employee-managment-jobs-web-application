# Generated by Django 4.2.23 on 2025-06-26 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='dob',
            new_name='Birthday',
        ),
    ]
