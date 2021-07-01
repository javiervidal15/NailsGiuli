# Generated by Django 3.0 on 2021-07-01 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='DayNotAvailable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DayTurn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=True)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='turns.Day')),
            ],
        ),
        migrations.CreateModel(
            name='gender_now',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='orientation_now',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('duration', models.PositiveIntegerField(default=30)),
                ('price', models.FloatField(blank=True, default=0, null=True)),
                ('max_turn_simultaneous', models.IntegerField(default=1)),
                ('max_days', models.IntegerField(default=7)),
                ('day_not_available', models.ManyToManyField(to='turns.DayNotAvailable')),
                ('days_turn', models.ManyToManyField(to='turns.DayTurn')),
            ],
        ),
        migrations.CreateModel(
            name='StateTurn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TypeUnavailableDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('all_services', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Assigned',
            fields=[
                ('stateturn_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='turns.StateTurn')),
            ],
            bases=('turns.stateturn',),
        ),
        migrations.CreateModel(
            name='Completed',
            fields=[
                ('stateturn_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='turns.StateTurn')),
            ],
            bases=('turns.stateturn',),
        ),
        migrations.CreateModel(
            name='NotAssisted',
            fields=[
                ('stateturn_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='turns.StateTurn')),
            ],
            bases=('turns.stateturn',),
        ),
        migrations.CreateModel(
            name='user_now',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='turns.gender_now')),
                ('orientation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='turns.orientation_now')),
            ],
        ),
        migrations.CreateModel(
            name='Turn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_turn', models.DateField()),
                ('paid', models.BooleanField(default=False)),
                ('duration', models.IntegerField()),
                ('start', models.CharField(max_length=10)),
                ('clients', models.ManyToManyField(to='turns.Client')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='turns.Service')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='turns.StateTurn')),
            ],
        ),
        migrations.AddField(
            model_name='dayturn',
            name='hours',
            field=models.ManyToManyField(to='turns.Hour'),
        ),
        migrations.AddField(
            model_name='daynotavailable',
            name='motive',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='turns.TypeUnavailableDay'),
        ),
    ]
