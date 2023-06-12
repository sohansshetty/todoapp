# Generated by Django 4.2.2 on 2023-06-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='value',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='tasks',
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(blank=True, to='todo.tag'),
        ),
    ]
