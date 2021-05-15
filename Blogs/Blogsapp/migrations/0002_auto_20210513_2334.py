# Generated by Django 3.1.6 on 2021-05-13 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('comment', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=1),
        ),
    ]
