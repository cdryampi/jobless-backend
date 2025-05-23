# Generated by Django 5.2.1 on 2025-05-13 08:59

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, help_text='Nombre del usuario', max_length=100, null=True, verbose_name='Nombre')),
                ('apellido', models.CharField(blank=True, help_text='Apellido del usuario', max_length=100, null=True, verbose_name='Apellido')),
                ('correo_electronico', models.EmailField(blank=True, help_text='Correo electrónico del usuario', max_length=254, null=True, unique=True, verbose_name='Correo electrónico')),
                ('resumen_habilidades', django_ckeditor_5.fields.CKEditor5Field(blank=True, help_text='Resumen de habilidades del usuario', null=True, verbose_name='Resumen de habilidades')),
                ('descripcion', django_ckeditor_5.fields.CKEditor5Field(blank=True, help_text='Descripción del usuario', null=True, verbose_name='Descripción')),
                ('profesion', models.CharField(choices=[('estudiante', 'Estudiante'), ('profesor', 'Profesor'), ('trabajador', 'Trabajador'), ('desempleado', 'Desempleado')], default='estudiante', help_text='Profesión del usuario', max_length=100, verbose_name='Profesión')),
                ('ciudad', models.CharField(blank=True, help_text='Ciudad del usuario', max_length=100, null=True, verbose_name='Ciudad')),
                ('edad', models.IntegerField(blank=True, help_text='Edad del usuario', null=True, verbose_name='Edad')),
                ('disponibilidad', models.CharField(blank=True, help_text='Disponibilidad del usuario', max_length=100, null=True, verbose_name='Disponibilidad')),
            ],
            options={
                'verbose_name': 'Perfil de usuario',
                'verbose_name_plural': 'Perfiles de usuario',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('guest', 'Guest'), ('test', 'Test')], default='guest', max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['username'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
