# Generated by Django 4.2.17 on 2024-12-04 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actorquote',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]