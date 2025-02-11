# Generated by Django 5.1.6 on 2025-02-11 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('vul_ok', models.BooleanField(default=False)),
                ('srv_name', models.CharField(max_length=100)),
                ('req_date', models.DateField()),
                ('sendmail_date', models.DateField()),
                ('adm_buseo', models.CharField(max_length=30)),
                ('adm_name', models.CharField(max_length=15)),
                ('srv_loc', models.CharField(max_length=50)),
                ('bigo', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
