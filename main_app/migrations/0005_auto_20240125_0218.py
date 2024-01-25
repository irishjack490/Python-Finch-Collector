# Generated by Django 3.2.12 on 2024-01-25 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_feeding'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watercup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='feeding',
            name='date',
            field=models.DateField(verbose_name='feeding date'),
        ),
        migrations.AddField(
            model_name='finch',
            name='watercups',
            field=models.ManyToManyField(to='main_app.Watercup'),
        ),
    ]
