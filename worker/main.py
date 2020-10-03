##############################
# COVID-19 risk area monitor #
##############################
import os
import django
from django.conf import settings
django.setup()

import re
import requests

from cram.models import Page, Subscription

DE_PAGE = Page.objects.get(id=1)
URL = DE_PAGE.url
XPATH_COUNTRY = DE_PAGE.xpath_country
REGEX_COUNTRY = DE_PAGE.regex_country
REGEX_TIME = DE_PAGE.regex_time

MY_SUBSCRIPTION = Subscription.objects.get(id=1)
COUNTRY = MY_SUBSCRIPTION.country

def get_xpath(country):
    return XPATH_COUNTRY.format(country)

def get_regex_country(country):
    return REGEX_COUNTRY.format(country)

def get_emails():
    return os.environ.get('EMAILS')

def fetch_url(url):
    response = requests.get(url)
    return response.text

def get_time(html):
    return re.search(REGEX_TIME, html).group()

def get_country_areas(html, country):
    return re.search(get_regex_country(country), html).group()

def main():
    html = fetch_url(URL)
    print('Time: {}'.format(get_time(html)))
    print(get_country_areas(html, COUNTRY))

if __name__ == '__main__':
    main()
