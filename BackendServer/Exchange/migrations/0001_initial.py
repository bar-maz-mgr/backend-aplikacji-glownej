# Generated by Django 3.1.2 on 2020-10-20 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'open'), (2, 'expired'), (3, 'closed')], default=1)),
                ('stock_amount', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=1000.0, max_digits=12)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SellOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('stock_amount', models.PositiveIntegerField(default=0)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'open'), (2, 'expired'), (3, 'closed')], default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('avail_amount', models.PositiveIntegerField(default=0)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='Exchange.company')),
            ],
        ),
        migrations.CreateModel(
            name='UserStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_amount', models.PositiveIntegerField(default=0)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userstocks', to='Exchange.stock')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userstocks', to='Exchange.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('buy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='Exchange.buyoffer')),
                ('sell', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='Exchange.selloffer')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='Exchange.profile')),
            ],
        ),
        migrations.AddField(
            model_name='selloffer',
            name='user_stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selloffers', to='Exchange.userstock'),
        ),
        migrations.AddField(
            model_name='buyoffer',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyoffers', to='Exchange.stock'),
        ),
        migrations.AddField(
            model_name='buyoffer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyoffers', to='Exchange.profile'),
        ),
    ]
