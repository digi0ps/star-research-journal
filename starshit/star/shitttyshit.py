from bs4 import BeautifulSoup
import os, re
from django.template.loader import render_to_string
from pprint import pprint


def render_the_shit_html(filename, filey):
    file = open(filename, 'r')
    soup = BeautifulSoup(file.read(), 'html.parser')

    table_header = soup.find("td", class_="h1").text

    tds = soup.find_all('td', class_='br1')
    rows = []
    for td in tds:
        row = 0
        url = '#'
        if td.find('span', class_='txt_n'):
            row = td.find_all('span', class_='txt_n')
            row = list(map(str, row))
            row = "<br />".join(row)
        for link in tds[5].next_siblings:
            if link.find('a') and link.find('a') != -1:
                url = link.find('a')['href']
        if row:
            context = {
                'content': row,
                'url': url
            }
            rows.append(context)
    context_ = {
        'rows': rows
    }
    html = render_to_string('archive.html', context_)
    wfilename = '/Users/digiops/Desktop/www.starresearchjournal.com/output'+filey
    wfile = file(wfilename, 'w')
    wffile.write(html)
    wfile.close()
    file.close()


def go_through_the_shit_files():
    files = os.listdir('/Users/digiops/Desktop/www.starresearchjournal.com2')
    for file in files:
        if re.match(r'20.+\.html', file):
            render_the_shit_html('/Users/digiops/Desktop/www.starresearchjournal.com2'+file, file)

go_through_the_shit_files()
