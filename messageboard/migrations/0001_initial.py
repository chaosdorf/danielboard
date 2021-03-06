# Generated by Django 2.1.3 on 2018-11-16 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent', models.DateTimeField(auto_now_add=True, help_text='The time when this post was created.')),
                ('title', models.CharField(help_text="The post's title.", max_length=500, null=True)),
                ('content', models.TextField(help_text="The post's content.")),
            ],
        ),
    ]
