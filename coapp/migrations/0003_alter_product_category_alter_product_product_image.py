# Generated by Django 4.1.4 on 2022-12-30 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coapp', '0002_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CR', 'Curd'), ('ML', 'Milk'), ('LS', 'Lassi'), ('MS', 'Milkshake'), ('PN', 'Paneer'), ('GH', 'Ghee'), ('CZ', 'Cheese'), ('IC', 'Ice-creams')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='product'),
        ),
    ]
