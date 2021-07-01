# Generated by Django 3.0 on 2021-07-01 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completed',
            name='stateturn_ptr',
        ),
        migrations.RemoveField(
            model_name='daynotavailable',
            name='motive',
        ),
        migrations.RemoveField(
            model_name='dayturn',
            name='day',
        ),
        migrations.RemoveField(
            model_name='dayturn',
            name='hours',
        ),
        migrations.RemoveField(
            model_name='notassisted',
            name='stateturn_ptr',
        ),
        migrations.RemoveField(
            model_name='service',
            name='day_not_available',
        ),
        migrations.RemoveField(
            model_name='service',
            name='days_turn',
        ),
        migrations.RemoveField(
            model_name='turn',
            name='clients',
        ),
        migrations.RemoveField(
            model_name='turn',
            name='service',
        ),
        migrations.RemoveField(
            model_name='turn',
            name='state',
        ),
        migrations.RemoveField(
            model_name='user_now',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user_now',
            name='orientation',
        ),
        migrations.DeleteModel(
            name='Assigned',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Completed',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.DeleteModel(
            name='DayNotAvailable',
        ),
        migrations.DeleteModel(
            name='DayTurn',
        ),
        migrations.DeleteModel(
            name='gender_now',
        ),
        migrations.DeleteModel(
            name='Hour',
        ),
        migrations.DeleteModel(
            name='NotAssisted',
        ),
        migrations.DeleteModel(
            name='orientation_now',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='StateTurn',
        ),
        migrations.DeleteModel(
            name='Turn',
        ),
        migrations.DeleteModel(
            name='TypeUnavailableDay',
        ),
        migrations.DeleteModel(
            name='user_now',
        ),
    ]
