##############################
# COVID-19 risk area monitor #
##############################

import os
import re
import requests

COUNTRY = 'Schweiz'
URL = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Risikogebiete_neu.html'
XPATH_COUNTRY = '//*[@id="main"]//ul/li[contains(.,"{}")]'
REGEX_COUNTRY = '<li>{}.*(\\n.*\\n)?</li>'
REGEX_TIME = '(?<=<p>Stand: ).*(?= Uhr</p>)'

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
