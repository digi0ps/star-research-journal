from bs4 import BeautifulSoup
import os, re


def render_the_shit_html(filename):
    file = open(filename, 'r')
    soup = BeautifulSoup(file.read(), 'html.parser')

    table_header = soup.find("td", class_="h1").text

    tds = soup.find_all('td', class_='br1')
    all_spans = []

    for td in tds:
        spans = 0
        if td.find('span', class_='txt_n'):
            spans = td.find_all('span', class_='txt_n')
            spans = list(map(str, spans))
            spans = "<br />".join(spans)
        if spans:
            all_spans.append(spans)

    f = open("output/"+filename, 'w')
    f.write('\n\n'.join(all_spans))
    f.close()
    file.close()


def go_through_the_shit_files():
    os.chdir('/Users/digiops/Desktop/www.starresearchjournal.com')
    files = os.listdir()
    for file in files:
        if re.match(r'20.+\.html', file):
            render_the_shit_html(file)

go_through_the_shit_files()
