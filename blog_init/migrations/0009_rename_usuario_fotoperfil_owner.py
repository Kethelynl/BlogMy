# Generated by Django 5.1.1 on 2024-09-12 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog_init", "0008_rename_owner_fotoperfil_usuario"),
    ]

    operations = [
        migrations.RenameField(
            model_name="fotoperfil",
            old_name="usuario",
            new_name="owner",
        ),
    ]
