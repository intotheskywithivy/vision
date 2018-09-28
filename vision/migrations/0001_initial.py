# Generated by Django 2.0.8 on 2018-09-28 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(blank=True, max_length=255, null=True)),
                ('post_body', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
