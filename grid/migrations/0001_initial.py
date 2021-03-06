# Generated by Django 3.1 on 2020-08-22 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='FirstGrid', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='GridElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grid.grid')),
            ],
        ),
    ]
