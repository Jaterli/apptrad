# Generated by Django 5.1.1 on 2024-09-26 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traductores', '0015_alter_perfilprofesional_lenguas_nativas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilprofesional',
            name='textos',
            field=models.TextField(blank=True, null=True),
        ),
    ]
