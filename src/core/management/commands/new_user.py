from datetime import timedelta, time, datetime

from django.core.mail import mail_admins
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.timezone import make_aware

from quiz.models import Result
from accounts.models import CustomUser

today = timezone.now()
tomorrow = today + timedelta(1)
today_start = make_aware(datetime.combine(today, time()))
today_end = make_aware(datetime.combine(tomorrow, time()))


class Command(BaseCommand):
    help = "Send Today's Orders Report to Admins"

    def handle(self, *args, **options):
        result = Result.objects.filter(update_timestamp__range=(today_start, today_end))
        users = CustomUser.objects.filter(is_activated=True)

        for user in users:
            if not result:
                subject = ('Exam')
                message = f"Dear {user}, You have to do any exam till midnight"
                mail_admins(subject=subject, message=message, html_message=None)

                self.stdout.write("E-mail to the student sent")
            else:
                self.stdout.write("All students did at least one exam.")
