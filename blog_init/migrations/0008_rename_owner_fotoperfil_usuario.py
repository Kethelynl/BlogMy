# Generated by Django 5.1.1 on 2024-09-12 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog_init", "0007_alter_fotoperfil_owner"),
    ]

    operations = [
        migrations.RenameField(
            model_name="fotoperfil",
            old_name="owner",
            new_name="usuario",
        ),
    ]
