# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('reply', models.TextField(verbose_name='Resposta')),
                ('correct', models.BooleanField(verbose_name='Correta?', default=False)),
                ('created', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Modificado em', auto_now=True)),
                ('author', models.ForeignKey(verbose_name='Autor', related_name='replies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Resposta',
                'verbose_name_plural': 'Respostas',
                'ordering': ['-correct', 'created'],
            },
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='Título', max_length=100)),
                ('body', models.TextField(verbose_name='Mensagem')),
                ('views', models.IntegerField(verbose_name='Visualizações', blank=True, default=0)),
                ('answers', models.IntegerField(verbose_name='Respostas', blank=True, default=0)),
                ('created', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Modificado em', auto_now=True)),
                ('author', models.ForeignKey(verbose_name='Autor', related_name='threads', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(verbose_name='Tags', to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.')),
            ],
            options={
                'verbose_name': 'Tópico',
                'verbose_name_plural': 'Tópicos',
                'ordering': ['-modified'],
            },
        ),
        migrations.AddField(
            model_name='reply',
            name='thread',
            field=models.ForeignKey(verbose_name='Tópico', related_name='replies', to='forum.Thread'),
        ),
    ]
