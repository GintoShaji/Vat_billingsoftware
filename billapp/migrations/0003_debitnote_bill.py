# Generated by Django 4.1.1 on 2024-04-30 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0002_debitnoteitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='debitnote',
            name='bill',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='billapp.purchasebill'),
            preserve_default=False,
        ),
    ]