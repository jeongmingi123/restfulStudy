# Generated by Django 3.1.7 on 2021-03-05 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_create_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_at'], 'verbose_name': '게시글'},
        ),
        migrations.AddField(
            model_name='post',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]
