# Generated by Django 5.1.1 on 2024-09-11 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog_init", "0003_topicos_delete_clienteuser"),
    ]

    operations = [
        migrations.CreateModel(
            name="Entrada",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                (
                    "imagem",
                    models.ImageField(
                        blank=True, null=True, upload_to="imagem_entrada/"
                    ),
                ),
                ("data_add", models.DateTimeField(auto_now_add=True)),
                (
                    "topic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog_init.topicos",
                    ),
                ),
            ],
        ),
    ]
