# Generated by Django 2.2.7 on 2020-03-31 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_apply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='apply',
            name='job',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='job', to='jobs.Jobs'),
        ),
    ]
