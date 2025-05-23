# Generated by Django 5.2.1 on 2025-05-13 08:59

import django.db.models.deletion
import django.utils.timezone
import multimedia_manager.utils
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Fecha de creación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, help_text='Fecha de modificación')),
                ('title', models.CharField(max_length=255, verbose_name='Título del Documento')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Carga')),
                ('file', models.FileField(help_text='Suba un archivo PDF.', upload_to='documents/', verbose_name='Archivo')),
                ('creado_por', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_creados', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Archivo de Documento',
                'verbose_name_plural': 'Archivos de Documentos',
            },
        ),
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Fecha de creación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, help_text='Fecha de modificación')),
                ('file', models.FileField(max_length=255, upload_to='media_files/', validators=[multimedia_manager.utils.validate_image_file])),
                ('title', models.CharField(blank=True, help_text='Título o descripción de la imagen.', max_length=255, null=True, verbose_name='Título')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('creado_por', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_creados', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
