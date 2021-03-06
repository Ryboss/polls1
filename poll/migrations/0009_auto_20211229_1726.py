# Generated by Django 3.2.5 on 2021-12-29 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poll', '0008_alter_question_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=100, verbose_name='Ваш ответ')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Results',
        ),
    ]
