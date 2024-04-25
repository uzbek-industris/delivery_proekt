# Generated by Django 4.2.6 on 2024-04-25 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('megapizza', '0010_tovar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tovar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='megapizza.tovar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='status',
            field=models.CharField(choices=[('0', 'принят'), ('1', 'на кухне'), ('2', 'у курьера'), ('3', 'доставлен'), ('4', 'отменён'), ('5', 'Не обработан')], max_length=3),
        ),
        migrations.DeleteModel(
            name='OrderStatus',
        ),
    ]