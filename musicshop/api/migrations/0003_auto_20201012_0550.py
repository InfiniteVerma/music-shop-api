# Generated by Django 3.1.2 on 2020-10-12 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_instrument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='typeOfIns',
            field=models.CharField(choices=[('guitar', 'Guitar'), ('piano', 'Piano'), ('flute', 'Flute'), ('keyb', 'keyb'), ('drum', 'drum')], max_length=20),
        ),
    ]
