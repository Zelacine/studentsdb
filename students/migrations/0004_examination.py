# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_student_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0430')),
                ('during_time', models.DateTimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0441\u0434\u0430\u0447\u0438')),
                ('teacher', models.CharField(max_length=256, verbose_name='\u041f\u0440\u0435\u043f\u043e\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c', blank=True)),
                ('group', models.ManyToManyField(to='students.Group', null=True, verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430', blank=True)),
            ],
            options={
                'verbose_name': '\u042d\u043a\u0437\u0430\u043c\u0435\u043d',
            },
        ),
    ]
