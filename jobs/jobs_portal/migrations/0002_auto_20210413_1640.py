# Generated by Django 3.1.4 on 2021-04-13 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='job',
            name='max_age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='min_age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='n_openings',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.IntegerField(),
        ),
    ]