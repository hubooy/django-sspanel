# Generated by Django 3.0.2 on 2020-03-02 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sspanel", "0033_auto_20200301_0829"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="ss_port",
            field=models.IntegerField(default=1025, unique=True, verbose_name="端口"),
        ),
    ]
