# Generated by Django 4.1.7 on 2023-04-19 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_field_formfield_form_header'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formfieldoption',
            old_name='field',
            new_name='fields',
        ),
    ]