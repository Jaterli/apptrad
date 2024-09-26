# Generated by Django 5.1.1 on 2024-09-26 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traductores', '0014_remove_combinacion_debug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilprofesional',
            name='lenguas_nativas',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='perfilprofesional',
            name='softwares',
            field=models.CharField(blank=True, help_text='Seleccione los softwares que utiliza', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='perfilprofesional',
            name='textos',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='traductor',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
