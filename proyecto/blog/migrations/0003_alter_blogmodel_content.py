# Generated by Django 4.1.7 on 2023-04-02 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='content',
            field=models.CharField(max_length=1000),
        ),
    ]
