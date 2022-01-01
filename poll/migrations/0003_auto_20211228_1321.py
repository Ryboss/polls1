# Generated by Django 3.2.5 on 2021-12-28 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_poll_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='type',
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('1', 'Ответ текстом'), ('2', 'Ответ с выбором одного варианте'), ('3', 'Ответ с выбором нескольких вариантов')], max_length=50, null=True),
        ),
    ]