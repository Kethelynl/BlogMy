# Generated by Django 5.1.1 on 2024-09-12 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog_init", "0010_alter_fotoperfil_owner"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Categorias",
        ),
        migrations.DeleteModel(
            name="FotoPerfil",
        ),
    ]
