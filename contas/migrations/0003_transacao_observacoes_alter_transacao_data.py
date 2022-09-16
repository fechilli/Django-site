# Generated by Django 4.1.1 on 2022-09-06 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_transacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacao',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
    ]