# Generated by Django 5.0.4 on 2024-04-23 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_options_alter_tag_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='scopes', through='articles.Scope', to='articles.tag'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.tag', verbose_name='Раздел'),
        ),
    ]
