# Generated by Django 3.1.1 on 2020-09-13 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, unique=True, verbose_name='用户名')),
                ('name', models.CharField(max_length=128, verbose_name='队伍名称')),
                ('victory', models.IntegerField(default=0, verbose_name='胜场数')),
                ('draw', models.IntegerField(default=0, verbose_name='平局数')),
                ('lose', models.IntegerField(default=0, verbose_name='负场数')),
                ('goals_num', models.IntegerField(default=0, verbose_name='进球数')),
                ('goals_conceded', models.IntegerField(default=0, verbose_name='失球数')),
            ],
            options={
                'verbose_name': '队伍',
                'verbose_name_plural': '队伍',
            },
        ),
    ]
