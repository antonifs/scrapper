from bs4 import BeautifulSoup
import urllib2

urls = [
        'http://resepkoki.co/tips-memilih-daging-ayam-segar-bebas-formalin/',
        ''
]

page = urllib2.urlopen("")
soup = BeautifulSoup(page, 'html.parser')

title = soup.find('h1', attrs={'class': 'entry-title'})
content = soup.find('div', attrs={'class': 'entry-content'})
content.findAll(['h3','p'])