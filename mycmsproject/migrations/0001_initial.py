# Generated by Django 3.1.14 on 2024-03-13 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='mycmsproject_poem', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(default='Title', max_length=50)),
                ('body', models.CharField(default='MyPoem', max_length=1000)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
