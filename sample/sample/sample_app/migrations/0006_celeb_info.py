# Generated by Django 4.1.4 on 2023-03-30 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sample_app", "0005_celeb_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="celeb",
            name="info",
            field=models.TextField(default="hei"),
            preserve_default=False,
        ),
    ]
