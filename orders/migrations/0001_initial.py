# Generated by Django 2.0.3 on 2020-05-29 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('SMALL', 'Small'), ('MEDIUM', 'Medium')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('SMALL', 'Small'), ('MEDIUM', 'Medium')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='SubIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='sub',
            name='ingredients',
            field=models.ManyToManyField(blank=True, related_name='pizzas', to='orders.SubIngredient'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='ingredients',
            field=models.ManyToManyField(blank=True, related_name='pizzas', to='orders.PizzaIngredient'),
        ),
        migrations.AddField(
            model_name='order',
            name='pizza',
            field=models.ManyToManyField(blank=True, related_name='pizzaOrders', to='orders.Pizza'),
        ),
        migrations.AddField(
            model_name='order',
            name='sub',
            field=models.ManyToManyField(blank=True, related_name='subOrders', to='orders.Sub'),
        ),
    ]
