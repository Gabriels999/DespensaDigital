# Generated by Django 4.0.5 on 2023-02-19 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_despensausuario_userstore'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='real_quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='target_quantity',
        ),
        migrations.AddField(
            model_name='userstore',
            name='real_quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userstore',
            name='target_quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
