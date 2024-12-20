# Generated by Django 5.1.4 on 2024-12-20 01:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_salao_cnpj"),
    ]

    operations = [
        migrations.AlterField(
            model_name="salao",
            name="cnpj",
            field=models.CharField(
                default="00000000000000",
                max_length=14,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_cnpj",
                        message="O CNPJ deve ter exatamente 14 dígitos numéricos.",
                        regex="^\\d{14}$",
                    )
                ],
            ),
        ),
    ]
