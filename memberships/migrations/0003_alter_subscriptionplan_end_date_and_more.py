# Generated by Django 4.1.7 on 2024-05-04 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0002_alter_pricing_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionplan',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='start_date',
            field=models.DateField(),
        ),
    ]
