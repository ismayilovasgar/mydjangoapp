# Generated by Django 3.2.9 on 2024-06-02 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_blog_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category'),
        ),
    ]
