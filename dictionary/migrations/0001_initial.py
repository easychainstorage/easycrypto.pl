# Generated by Django 4.0.9 on 2023-07-08 16:59

from django.db import migrations, models
import django.db.models.manager
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Glossary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('body', django_quill.fields.QuillField(blank=True, default='', null=True)),
                ('place_news', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N'), ('O', 'O'), ('P', 'P'), ('Q', 'Q'), ('R', 'R'), ('S', 'S'), ('T', 'T'), ('U', 'U'), ('V', 'V'), ('W', 'W'), ('X', 'X'), ('Y', 'Y'), ('Z', 'Z')], default='A', max_length=10)),
                ('level', models.CharField(choices=[('basic', 'Podstawowy'), ('medium', 'Średniozaawansowany'), ('hard', 'Zaawansowany')], default='Podstawowy', max_length=20)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
