# Generated by Django 4.2.4 on 2023-08-20 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userfile', '0008_alter_product_sub_cat_product_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.CharField(default='product_maneger', max_length=100),
        ),
    ]
