# Generated by Django 4.1.4 on 2022-12-13 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='Stok',
            new_name='stok',
        ),
    ]