# Generated by Django 2.2.6 on 2019-11-04 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20191104_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='creator',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='participant',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='numOfCreatedEvents',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='numOfParticipatingEvents',
            field=models.IntegerField(),
        ),
    ]
