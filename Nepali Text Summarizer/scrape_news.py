import urllib
import re

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def get_content_onlinekhabar(link):
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, features="lxml")
    text =''
    for tex_ in soup.find_all("p")[:-1]:
        text = text + " " + tex_.getText()
        return ''.join(text)

def get_content_ekantipur(link):
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, features="lxml")
    try:
        for text_ in soup.find_all(attrs={'class' : 'description'}):
            return text_.text[:text_.text.find('प्रकाशित ')]
    except:
        raise ValueError('Unable to extract from the link given')