# Generated by Django 4.2.6 on 2024-04-25 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megapizza', '0005_alter_orderstatus_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
