# Generated by Django 4.1.7 on 2023-04-21 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_field_formfieldoption_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfieldsinoption',
            name='field_option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_option', to='main.formfieldoption'),
        ),
    ]
