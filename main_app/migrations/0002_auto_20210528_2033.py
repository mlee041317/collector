# Generated by Django 3.2.3 on 2021-05-28 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='many',
            name='name',
        ),
        migrations.AddField(
            model_name='many',
            name='moment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.moment'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='many',
            name='feeling',
            field=models.CharField(choices=[('H', 'Happy'), ('Sa', 'Sad'), ('Su', 'Surprised'), ('A', 'Angry'), ('C', 'Confused')], default='H', max_length=2),
        ),
        migrations.AlterField(
            model_name='many',
            name='people',
            field=models.CharField(max_length=250, verbose_name='name'),
        ),
    ]
