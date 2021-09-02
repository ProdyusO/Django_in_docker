# Generated by Django 3.2.6 on 2021-09-01 10:12

import core.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=core.utils.generate_uuid, unique=True)),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, null=True)),
                ('level', models.PositiveSmallIntegerField(choices=[(0, 'Basic'), (1, 'Middle'), (2, 'Advanced')], default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'New'), (1, 'Finished')], default=0)),
                ('uuid', models.UUIDField(db_index=True, default=core.utils.generate_uuid, unique=True)),
                ('current_order_number', models.PositiveSmallIntegerField(null=True)),
                ('num_correct_answers', models.PositiveSmallIntegerField(default=0)),
                ('num_incorrect_answers', models.PositiveSmallIntegerField(default=0)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='quiz.exam')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True)),
                ('order_num', models.PositiveSmallIntegerField()),
                ('text', models.CharField(max_length=2048)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.exam')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1024)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='quiz.question')),
            ],
        ),
    ]
