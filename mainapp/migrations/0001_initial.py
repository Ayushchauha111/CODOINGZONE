# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-14 19:53
from __future__ import unicode_literals

import datetime
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
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_part1', models.IntegerField()),
                ('score_part2', models.IntegerField()),
                ('ans_part1', models.CharField(max_length=256)),
                ('ans_part2', models.CharField(max_length=256)),
                ('question_name', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='teaminfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member1_name', models.CharField(max_length=256)),
                ('member1_rollno', models.PositiveIntegerField()),
                ('member1_phone', models.PositiveIntegerField()),
                ('member1_branch', models.CharField(max_length=256)),
                ('member2_name', models.CharField(max_length=256)),
                ('member2_rollno', models.PositiveIntegerField()),
                ('member2_phone', models.PositiveIntegerField()),
                ('member2_branch', models.CharField(max_length=256)),
                ('collegename', models.CharField(max_length=256)),
                ('start_time', models.DateTimeField(blank=True, default=None, null=True)),
                ('totalscore', models.PositiveIntegerField(blank=True, default=0)),
                ('last_submit_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('total_time', models.DurationField(blank=True, default=datetime.timedelta(0))),
                ('ques1_part1_score', models.PositiveIntegerField(blank=True, default=0)),
                ('ques1_part2_score', models.PositiveIntegerField(blank=True, default=0)),
                ('ques2_part1_score', models.PositiveIntegerField(blank=True, default=0)),
                ('ques2_part2_score', models.PositiveIntegerField(blank=True, default=0)),
                ('ques3_part1_score', models.PositiveIntegerField(blank=True, default=0)),
                ('ques3_part2_score', models.PositiveIntegerField(blank=True, default=0)),
                ('ques4_part1_score', models.PositiveIntegerField(blank=True, default=0)),
                ('ques4_part2_score', models.PositiveIntegerField(blank=True, default=0)),
                ('ques5_part1_score', models.PositiveIntegerField(blank=True, default=0)),
                ('ques5_part2_score', models.PositiveIntegerField(blank=True, default=0)),
                ('ques6_part1_score', models.PositiveIntegerField(blank=True, default=0)),
                ('ques6_part2_score', models.PositiveIntegerField(blank=True, default=0)),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
