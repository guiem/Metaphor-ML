# Generated by Django 2.0.2 on 2018-02-05 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metaphor', '0002_dictionary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='req_date',
            field=models.DateTimeField(verbose_name='date requested'),
        ),
    ]