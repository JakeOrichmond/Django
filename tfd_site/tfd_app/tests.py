import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Type
# Create your tests here.


class TypeMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for types whose pub_date is in the future.
        """
        time=timezone.now() + datetime.timedelta(days=30)
        future_type = Type(pub_date=time)
        self.assertEqual(future_type.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published recently() should return False for types whose pub_date is older than 1 day
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_type = Type(pub_date=time)
        self.assertEqual(old_type.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for types whose pub_date is within the last day.
        """

    def time = timezone.now() - datetime.timedelta(hours=1)
    recent_type = Type(pub_date=time)
    self.assertEqual(recent_type.was_published_recently(), True)