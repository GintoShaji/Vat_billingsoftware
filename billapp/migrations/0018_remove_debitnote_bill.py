# Generated by Django 4.1.1 on 2024-05-04 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0017_debitnote_bill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='debitnote',
            name='bill',
        ),
    ]