# Generated by Django 2.2 on 2019-06-09 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='type',
            field=models.IntegerField(choices=[(0, 'Conferência'), (1, 'Periódico'), (2, 'Resumo')]),
        ),
    ]