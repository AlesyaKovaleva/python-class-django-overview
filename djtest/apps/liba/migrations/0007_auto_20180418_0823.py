# Generated by Django 2.0 on 2018-04-18 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liba', '0006_auto_20180418_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_id',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='books', to='liba.Author'),
        ),
    ]
