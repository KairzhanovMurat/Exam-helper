# Generated by Django 4.1.1 on 2022-09-15 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ans_name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='question',
            name='quest_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subj_name',
            field=models.CharField(max_length=100),
        ),
    ]