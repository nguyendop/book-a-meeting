# Generated by Django 4.0.2 on 2022-03-15 07:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0012_alter_customuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]