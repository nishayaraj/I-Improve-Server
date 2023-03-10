# Generated by Django 4.1.6 on 2023-02-07 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('due', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           to='iimproveapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='Retro',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('went_well', models.TextField(max_length=500)),
                ('to_improve', models.TextField(max_length=500)),
                ('action_item', models.TextField(max_length=500)),
                ('date', models.DateField()),
                ('status', models.BooleanField()),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           to='iimproveapi.goal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           to='iimproveapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='KeyMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           to='iimproveapi.goal')),
            ],
        ),
        migrations.CreateModel(
            name='GoalTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           to='iimproveapi.goal')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                          to='iimproveapi.tag')),
            ],
        ),
        migrations.AddField(
            model_name='goal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to='iimproveapi.user'),
        ),
    ]
