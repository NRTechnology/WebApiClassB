# Generated by Django 4.0.4 on 2022-05-28 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nim', models.CharField(max_length=10)),
                ('Nama', models.CharField(max_length=255)),
                ('TmpLahir', models.CharField(max_length=255)),
                ('TglLahir', models.DateField()),
                ('Alamat', models.CharField(max_length=255)),
                ('Kelamin', models.CharField(choices=[('LK', 'Laki-Laki'), ('PR', 'Perempuan')], max_length=2)),
            ],
        ),
    ]
