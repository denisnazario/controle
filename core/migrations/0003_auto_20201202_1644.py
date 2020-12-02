# Generated by Django 3.1.3 on 2020-12-02 16:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_budget_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentsplit',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='budget',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='transact',
            name='date_paid',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
