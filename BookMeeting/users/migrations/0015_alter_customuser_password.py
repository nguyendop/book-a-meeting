from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0014_alter_customuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
