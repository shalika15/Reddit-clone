# Generated by Django 2.0.7 on 2018-08-08 06:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('vote_total', models.IntegerField(default=1)),
                ('author', models.ForeignKey(on_delete=0, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
