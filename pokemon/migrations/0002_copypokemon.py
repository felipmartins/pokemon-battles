# Generated by Django 4.0.6 on 2022-07-10 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CopyPokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type_1', models.CharField(max_length=50)),
                ('type_2', models.CharField(blank=True, max_length=50)),
                ('total', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('atk', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('sp_atk', models.IntegerField()),
                ('sp_def', models.IntegerField()),
                ('speed', models.IntegerField()),
            ],
        ),
    ]