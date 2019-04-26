# Generated by Django 2.2 on 2019-04-26 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
        ('study_group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('role', models.IntegerField(choices=[('0', 'Graduação'), ('1', 'Mestrado'), ('2', 'Doutorado'), ('3', 'Pós-doutorado')])),
                ('project', models.ManyToManyField(to='project.Project')),
                ('study_group', models.ManyToManyField(to='study_group.StudyGroup')),
            ],
        ),
    ]
