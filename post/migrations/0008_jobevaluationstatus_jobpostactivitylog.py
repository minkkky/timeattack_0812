# Generated by Django 4.0 on 2022-07-22 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('post', '0007_jobpostactivity_job_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobEvaluationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'job_evaluation_status',
            },
        ),
        migrations.CreateModel(
            name='JobPostActivityLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_date', models.DateTimeField(auto_now_add=True)),
                ('interviewer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user')),
                ('job_evaluation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.jobevaluationstatus')),
                ('job_post_activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.jobpostactivity')),
            ],
            options={
                'db_table': 'job_post_activity_log',
            },
        ),
    ]
