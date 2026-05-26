from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("opcalendar", "0027_eventmember_comment_eventmember_status_usersettings"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="ping_here",
            field=models.BooleanField(
                default=False,
                help_text="Ping @here on Discord when this event is posted",
            ),
        ),
    ]
