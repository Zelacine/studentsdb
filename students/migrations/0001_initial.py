# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_exam', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0430')),
                ('during_time', models.DateTimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0441\u0434\u0430\u0447\u0438')),
                ('teacher', models.CharField(max_length=256, verbose_name='\u041f\u0440\u0435\u043f\u043e\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c', blank=True)),
            ],
            options={
                'verbose_name': '\u042d\u043a\u0437\u0430\u043c\u0435\u043d',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('notes', models.TextField(verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0437\u0430\u043c\u0435\u0442\u043a\u0438', blank=True)),
            ],
            options={
                'verbose_name': '\u0413\u0440\u0443\u043f\u0430',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256, verbose_name='\u0418\u043c\u044f')),
                ('last_name', models.CharField(max_length=256, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('middle_name', models.CharField(default=b'', max_length=256, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e', blank=True)),
                ('birthday', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('photo', models.ImageField(upload_to=b'', null=True, verbose_name='\u0424\u043e\u0442\u043e', blank=True)),
                ('ticket', models.CharField(max_length=256, verbose_name='\u0411\u0438\u043b\u0435\u0442')),
                ('notes', models.TextField(verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0437\u0430\u043c\u0435\u0442\u043a\u0438', blank=True)),
                ('student_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0413\u0440\u0443\u043f\u0430', to='students.Group', null=True)),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='students.Student', verbose_name='\u0421\u0442\u0430\u0440\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='examination',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='students.Group', unique=True, verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430'),
        ),
    ]
