# Generated by Django 3.0.2 on 2020-02-20 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0007_delete_session_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('cinema', models.DecimalField(decimal_places=0, max_digits=3)),
                ('price', models.CharField(default='$14.00', max_length=8)),
                ('booking_link', models.TextField(default='/bookings/')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Movies.Movie_Info')),
            ],
        ),
    ]