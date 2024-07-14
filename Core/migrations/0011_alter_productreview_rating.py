# Generated by Django 5.0.6 on 2024-07-14 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0010_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], default=None),
        ),
    ]
