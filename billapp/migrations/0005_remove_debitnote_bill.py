# Generated by Django 4.1.1 on 2024-04-30 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0004_alter_debitnote_bill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='debitnote',
            name='bill',
        ),
    ]
