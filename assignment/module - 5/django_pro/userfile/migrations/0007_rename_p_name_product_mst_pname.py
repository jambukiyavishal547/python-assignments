# Generated by Django 4.2.4 on 2023-08-19 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userfile', '0006_product_mst_p_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_mst',
            old_name='p_name',
            new_name='pname',
        ),
    ]
