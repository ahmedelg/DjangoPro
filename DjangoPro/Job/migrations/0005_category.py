# Generated by Django 4.2.7 on 2023-11-07 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0004_job_experience_job_published_at_job_salary_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]
