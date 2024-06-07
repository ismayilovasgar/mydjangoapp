# Generated by Django 3.2.9 on 2024-06-02 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_blog_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category_id',
        ),
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(to='myapp.Category'),
        ),
    ]