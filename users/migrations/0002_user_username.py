# Generated by Django 2.0.7 on 2018-07-25 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, max_length=150, unique=True),
            preserve_default=False,
        ),
    ]
