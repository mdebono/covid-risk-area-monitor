import unittest

import main

class TestMain(unittest.TestCase):
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
