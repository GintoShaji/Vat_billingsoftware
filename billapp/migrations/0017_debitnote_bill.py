# Generated by Django 4.1.1 on 2024-05-04 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0016_alter_debitnote_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='debitnote',
            name='bill',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='billapp.purchasebill'),
            preserve_default=False,
        ),
    ]
