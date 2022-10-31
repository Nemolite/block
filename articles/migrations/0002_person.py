# Generated by Django 4.1.1 on 2022-10-02 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Персона')),
                ('bron', models.DateField(verbose_name='Дата рождения')),
                ('locic', models.BooleanField()),
            ],
        ),
    ]
