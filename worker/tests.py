import unittest

import worker.main as main
from cram.models import Page, Subscription

class TestMain(unittest.TestCase):
    def setUp(self):
        p = Page(url='http://example.com', country='XX')
        p.xpath_country = '//*[@id="main"]//ul/li[contains(.,"{}")]'
        p.regex_country = '<li>{}.*(\\n.*\\n)?</li>'
        p.regex_time = '(?<=<p>Stand: ).*(?= Uhr</p>)'
        p.save()
        s = Subscription(country='XXX')
        s.save()

    def test_get_xpath(self):
        self.assertEqual(main.get_xpath('XXX'), '//*[@id="main"]//ul/li[contains(.,"XXX")]')

    def test_get_regex_country(self):
        self.assertEqual(main.get_regex_country('XXX'), '<li>XXX.*(\\n.*\\n)?</li>')

    def test_get_emails(self):
        self.assertIsNotNone(main.get_emails())

    def test_fetch_url(self):
        self.assertIsNotNone(main.fetch_url(main.URL))

    def test_get_time(self):
        html = '<html><body><p>Stand: 01.01.1970, 00:00 Uhr</p></body></html>'
        self.assertEqual(main.get_time(html), '01.01.1970, 00:00')

    def test_get_country_area(self):
        html = '<html><body><div id="main"><ul><li>XXX:<ul><li>YYY</li><li>ZZZ</li></ul></li></ul></div></body></html>'
        self.assertEqual(main.get_country_areas(html, 'XXX'), '<li>XXX:<ul><li>YYY</li><li>ZZZ</li></ul></li>')

if __name__ == '__main__':
    unittest.main()
