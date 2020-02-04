# Generated by Django 2.1 on 2020-02-04 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banglore_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('experience', models.IntegerField()),
                ('domain', models.CharField(max_length=100)),
                ('skill', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Chennai_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('experience', models.IntegerField()),
                ('domain', models.CharField(max_length=100)),
                ('skill', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hyderabad_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('experience', models.IntegerField()),
                ('domain', models.CharField(max_length=100)),
                ('skill', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pune_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('experience', models.IntegerField()),
                ('domain', models.CharField(max_length=100)),
                ('skill', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Registration_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=20)),
                ('emailid', models.EmailField(max_length=50)),
                ('mobileno', models.BigIntegerField()),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
