# Generated by Django 4.2.6 on 2023-11-26 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_title', models.CharField(max_length=200)),
                ('program_date', models.DateField()),
                ('prepared_by', models.CharField(max_length=100)),
                ('summary', models.TextField()),
                ('additional_comments', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
