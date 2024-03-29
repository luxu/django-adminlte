# Generated by Django 4.1.12 on 2024-01-04 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_city_options_remove_city_name_city_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em'),
        ),
        migrations.AddField(
            model_name='city',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Atualizado em'),
        ),
        migrations.AddField(
            model_name='city',
            name='status',
            field=models.BooleanField(choices=[(True, 'Ativa'), (False, 'Inativa')], default=True),
        ),
        migrations.CreateModel(
            name='Pecas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Atualizado em')),
                ('status', models.BooleanField(choices=[(True, 'Ativa'), (False, 'Inativa')], default=True)),
                ('data', models.DateField(verbose_name='Date')),
                ('veiculo', models.CharField(choices=[('C', 'Carro'), ('M', 'Moto')], max_length=1, verbose_name='Vehicle')),
                ('proxtroca', models.IntegerField(default=1, verbose_name='Next Exchange')),
                ('troca', models.IntegerField(default=1, verbose_name='change')),
                ('total', models.CharField(blank=True, max_length=100, null=True, verbose_name='Total')),
                ('city', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.city', verbose_name='Locality')),
            ],
            options={
                'verbose_name': 'Peça',
                'verbose_name_plural': 'Peças',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Itenspecas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Descrição')),
                ('price', models.CharField(blank=True, max_length=100, null=True, verbose_name='Preço')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantidade Comprada')),
                ('subtotal', models.CharField(blank=True, max_length=100, null=True, verbose_name='Sub-Total')),
                ('pecas', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.pecas', verbose_name='Peças')),
            ],
            options={
                'verbose_name': 'Item Peça',
                'verbose_name_plural': 'Itens Peças',
                'ordering': ['-id'],
            },
        ),
    ]
