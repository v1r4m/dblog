# Generated by Django 4.2.1 on 2023-05-10 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('templateId', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TextField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Xpos1', models.IntegerField()),
                ('Xpos2', models.IntegerField()),
                ('Ypos1', models.IntegerField()),
                ('Ypos2', models.IntegerField()),
                ('Question', models.TextField()),
                ('templateId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kokoo.template')),
            ],
        ),
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optionDescription', models.TextField()),
                ('Xpos1', models.IntegerField()),
                ('Xpos2', models.IntegerField()),
                ('Ypos1', models.IntegerField()),
                ('Ypos2', models.IntegerField()),
                ('fieldId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kokoo.selectfield')),
                ('templateId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kokoo.template')),
            ],
        ),
        migrations.AddField(
            model_name='selectfield',
            name='templateId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kokoo.template'),
        ),
    ]
