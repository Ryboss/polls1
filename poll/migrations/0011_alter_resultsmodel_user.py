# Generated by Django 3.2.5 on 2021-12-30 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0010_alter_resultsmodel_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultsmodel',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]