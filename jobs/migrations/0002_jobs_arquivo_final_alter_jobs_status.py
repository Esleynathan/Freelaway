# Generated by Django 4.1.7 on 2023-02-25 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='arquivo_final',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='status',
            field=models.CharField(choices=[('C', 'Em criação'), ('AA', 'Aguardando aprovação'), ('F', 'Finalizado')], default='C', max_length=2),
        ),
    ]
