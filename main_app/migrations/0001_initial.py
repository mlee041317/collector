# Generated by Django 3.2.3 on 2021-05-27 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Many',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(verbose_name='date')),
                ('people', models.CharField(max_length=250)),
                ('feeling', models.CharField(choices=[('H', 'Happy'), ('Sa', 'Sad'), ('Su', 'Surprised'), ('A', 'Angry'), ('C', 'Confused')], default='H', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Moment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('month', models.TextField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
