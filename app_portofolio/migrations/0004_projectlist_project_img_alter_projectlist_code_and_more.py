# Generated by Django 4.0.4 on 2022-07-01 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_portofolio', '0003_alter_techchoices_tech_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectlist',
            name='project_img',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='projectlist',
            name='code',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='projectlist',
            name='web_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
