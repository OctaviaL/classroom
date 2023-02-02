# Generated by Django 4.1.6 on 2023-02-02 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('test1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.TextField()),
                ('post_comm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='test1.comment')),
            ],
        ),
    ]
