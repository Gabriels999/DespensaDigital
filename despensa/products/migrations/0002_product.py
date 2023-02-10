# Generated by Django 4.0.5 on 2023-02-10 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=132)),
                ('price', models.FloatField()),
                ('target_quantity', models.IntegerField()),
                ('real_quantity', models.IntegerField()),
                ('type', models.CharField(choices=[('CONGELADOS', 'Congelados'), ('REFRIGERADOS', 'Refrigerados'), ('HORTIFRUTI', 'Hortifruti'), ('FRUTAS', 'Frutas'), ('SECOS', 'Secos'), ('LIMPEZA', 'Limpeza'), ('HIGIENE', 'Higiene')], default=False, max_length=64)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]