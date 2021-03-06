# Generated by Django 2.2.14 on 2020-07-14 01:51

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('url', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), size=None)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Nature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=40)),
                ('descr_en', models.CharField(max_length=100)),
                ('descr_de', models.CharField(max_length=100)),
                ('descr_fr', models.CharField(max_length=100)),
                ('descr_it', models.CharField(max_length=100)),
                ('descr_rm', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['index'],
            },
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=40)),
                ('descr_en', models.CharField(max_length=100)),
                ('descr_de', models.CharField(max_length=100)),
                ('descr_fr', models.CharField(max_length=100)),
                ('descr_it', models.CharField(max_length=100)),
                ('descr_rm', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['index'],
            },
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revision_type', models.CharField(choices=[('NOTE', 'Note'), ('ACTION', 'Action'), ('PROGRESS', 'Progress'), ('FEEDBACK', 'Feedback'), ('SOLVED', 'Solved'), ('CLOSED', 'Closed')], default='NOTE', max_length=10)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('alert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alerts.Alert')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='alert',
            name='nature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='alerts.Nature'),
        ),
        migrations.AddField(
            model_name='alert',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='alerts.Origin'),
        ),
    ]
