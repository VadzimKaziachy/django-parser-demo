# Generated by Django 3.0.6 on 2020-05-13 13:45

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twenty_first_century', '0002_auto_20200126_1024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'ordering': ('pk',), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='parserproductmodel',
            options={'ordering': ('pk',), 'verbose_name': 'Parser product', 'verbose_name_plural': 'Parser products'},
        ),
        migrations.AlterModelOptions(
            name='productmodel',
            options={'ordering': ('pk',), 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='parserproductmodel',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='ScrapyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('job_id', models.CharField(max_length=1000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twenty_first_century.CategoryModel')),
            ],
            options={
                'verbose_name': 'Scrapy model',
                'verbose_name_plural': 'Scrapy models',
                'ordering': ('pk',),
            },
        ),
    ]
