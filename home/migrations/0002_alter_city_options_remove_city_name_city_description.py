# Generated by Django 4.1.12 on 2024-01-04 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['-id'], 'verbose_name': 'Localidade', 'verbose_name_plural': 'Localidades'},
        ),
        migrations.RemoveField(
            model_name='city',
            name='name',
        ),
        migrations.AddField(
            model_name='city',
            name='description',
            field=models.CharField(max_length=100, null=True, verbose_name='Description'),
        ),
    ]
