# Generated by Django 4.1.6 on 2023-02-13 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('is_published', models.BooleanField()),
                ('image', models.ImageField(upload_to='')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.category')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
    ]
