# Generated by Django 4.0.4 on 2022-07-01 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TechChoices',
            fields=[
                ('tech_name', models.CharField(max_length=15, unique=True)),
                ('tech_desc', models.TextField(blank=True, null=True)),
                ('tech_slug', models.SlugField(max_length=15, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=50, null=True)),
                ('author', models.CharField(default='torik135', max_length=50)),
                ('project_desc', models.TextField(blank=True, null=True)),
                ('project_img', models.URLField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('code', models.URLField(blank=True, max_length=250, null=True)),
                ('web_link', models.URLField(blank=True, null=True)),
                ('project_type', models.CharField(blank=True, choices=[('FE', 'Front End'), ('BE', 'Back End'), ('FS', 'Full Stack'), ('PL', 'Plain / Native')], max_length=150, null=True)),
                ('tech', models.ManyToManyField(to='app_portofolio.techchoices')),
            ],
        ),
    ]
