# Generated by Django 4.2.4 on 2023-09-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Price')),
                ('category', models.CharField(choices=[('ACTION', 'Action'), ('HOME', 'Home'), ('PYTHON', 'Python'), ('PHP', 'Php'), ('JAVA', 'Java')], max_length=50, verbose_name='Category')),
                ('description', models.TextField(verbose_name='Description')),
                ('stock', models.IntegerField(default=0, verbose_name='Stock')),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Cost')),
                ('create_At', models.DateTimeField(auto_now_add=True, verbose_name='Create AT')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]
