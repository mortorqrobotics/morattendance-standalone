# Generated by Django 2.2.3 on 2019-08-02 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190802_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='stud_id',
            field=models.IntegerField(blank=True, help_text='Type in your 10-Digit ID. Used for logging attendance', null=True),
        ),
    ]
