# Generated by Django 3.0.3 on 2020-02-25 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap', '0002_rawdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawdata',
            name='link_type',
            field=models.CharField(choices=[('Website', 'Website'), ('Filehoster', 'Filehoster'), ('Torrent', 'Torrent')], default='Website', max_length=20),
        ),
    ]
