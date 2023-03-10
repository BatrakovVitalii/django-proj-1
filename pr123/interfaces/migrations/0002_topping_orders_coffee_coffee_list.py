# Generated by Django 4.1.5 on 2023-01-31 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interfaces', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_topping', models.CharField(max_length=32)),
                ('price', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField()),
                ('client_name', models.CharField(max_length=24)),
                ('order_list', models.ManyToManyField(to='interfaces.coffee')),
            ],
        ),
        migrations.AddField(
            model_name='coffee',
            name='coffee_list',
            field=models.ManyToManyField(to='interfaces.topping'),
        ),
    ]
