# Generated by Django 5.0.6 on 2024-07-08 12:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post_machine', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=200)),
                ('size', models.IntegerField()),
                ('order_datetime', models.DateTimeField(verbose_name='date published')),
                ('open_datetime', models.DateTimeField(verbose_name='date published')),
                ('status', models.BooleanField(default=False)),
                ('post_machine_recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_machine.postmachine')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]