# Generated by Django 4.0.9 on 2023-07-16 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook', '0005_ebook_small_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='EbookEmails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
            ],
        ),
    ]
