# Generated by Django 4.0.4 on 2022-05-24 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='built_at',
            field=models.DateField(verbose_name='Barpo qilingan vaqti'),
        ),
        migrations.AlterField(
            model_name='travel',
            name='updated_at',
            field=models.DateField(verbose_name='Yangilangan vaqti'),
        ),
    ]
