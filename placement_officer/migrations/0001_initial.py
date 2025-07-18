# Generated by Django 5.1.1 on 2025-06-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Category_1', 'Category 1'), ('Category_2', 'Category 2'), ('Category_3', 'Category 3'), ('Category_4', 'Category 4')], max_length=20)),
                ('batch', models.CharField(max_length=50)),
                ('minimum_academic_attendance', models.FloatField(blank=True, null=True)),
                ('minimum_academic_performance', models.FloatField(blank=True, null=True)),
                ('minimum_training_attendance', models.FloatField(blank=True, null=True)),
                ('minimum_training_performance', models.FloatField(blank=True, null=True)),
            ],
            options={
                'ordering': ['category'],
                'unique_together': {('category', 'batch')},
            },
        ),
    ]
