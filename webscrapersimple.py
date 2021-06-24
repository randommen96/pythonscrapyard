import bs4
import lxml
import requests

listofpages = []

def select_authors(listofpages):
    for page in listofpages:
        authors = page.select(".author")
        authorset = set()
        for author in authors:
            authorset.add(str(author.text))
    
        print(authorset)

def get_pages():
    global listofpages
    number = 1
    while True:
        scrapesource = "http://quotes.toscrape.com/page/" + str(number)
        quotesdata = requests.get(url=scrapesource)
        quotessoup = bs4.BeautifulSoup(quotesdata.text, 'lxml')
        if "No quotes found!" in str(quotessoup):
            break
        number += 1
        listofpages.append(quotessoup)
        print(scrapesource)

get_pages()
print("amount of pages scanned:" + str(len(listofpages)))
select_authors(listofpages)
