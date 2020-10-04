import unittest
import os

def set_os_environ_if_empty(var, default):
    if var not in os.environ:
        os.environ[var] = default

set_os_environ_if_empty('DJANGO_SECRET_KEY', 'XXX')
set_os_environ_if_empty('EMAILS', 'XXX')
set_os_environ_if_empty('DJANGO_SETTINGS_MODULE', 'web.settings')

import django
from django.conf import settings
django.setup()

from cram.models import User, Page, Subscription

u = User(email="test@example.com")
u.save()
p = Page(url='http://example.com', country='XX')
p.xpath_country = '//*[@id="main"]//ul/li[contains(.,"{}")]'
p.regex_country = '<li>{}.*(\\n.*\\n)?</li>'
p.regex_time = '(?<=<p>Stand: ).*(?= Uhr</p>)'
p.save()
s = Subscription(country='XXX', page=p, user=u)
s.save()

import worker

class TestWorker(unittest.TestCase):
    def test_get_xpath(self):
        self.assertEqual(worker.get_xpath('XXX'), '//*[@id="main"]//ul/li[contains(.,"XXX")]')

    def test_get_regex_country(self):
        self.assertEqual(worker.get_regex_country('XXX'), '<li>XXX.*(\\n.*\\n)?</li>')

    def test_get_emails(self):
        self.assertIsNotNone(worker.get_emails())

    def test_fetch_url(self):
        self.assertIsNotNone(worker.fetch_url(worker.URL))

    def test_get_time(self):
        html = '<html><body><p>Stand: 01.01.1970, 00:00 Uhr</p></body></html>'
        self.assertEqual(worker.get_time(html), '01.01.1970, 00:00')

    def test_get_country_area(self):
        html = '<html><body><div id="main"><ul><li>XXX:<ul><li>YYY</li><li>ZZZ</li></ul></li></ul></div></body></html>'
        self.assertEqual(worker.get_country_areas(html, 'XXX'), '<li>XXX:<ul><li>YYY</li><li>ZZZ</li></ul></li>')

if __name__ == '__main__':
    unittest.main()
