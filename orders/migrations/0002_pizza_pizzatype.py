# Generated by Django 2.0.3 on 2020-05-30 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='pizzaType',
            field=models.CharField(choices=[('Regular', 'Regular'), ('Sicilian', 'Sicilian')], default='regular', max_length=10),
            preserve_default=False,
        ),
    ]
