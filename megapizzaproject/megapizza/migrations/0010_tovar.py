# Generated by Django 4.2.6 on 2024-04-25 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megapizza', '0009_alter_orderinfo_client_alter_orderinfo_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('fullname', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='megapizza/static/images')),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
    ]