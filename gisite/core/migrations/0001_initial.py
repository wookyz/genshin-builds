# Generated by Django 3.1.7 on 2021-03-30 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=50)),
                ('guide', models.TextField(blank=True, null=True)),
                ('characters', models.JSONField()),
            ],
        ),
    ]
