from requests import get
from bs4 import BeautifulSoup
scrape = []
url = "https://www.ncbi.nlm.nih.gov/pubmed/"
for i in range(1,100):
    response = get(url+str(i))
    html_soup = BeautifulSoup(response.text,'html.parser')
    abstract = html_soup.find_all('div',class_="abstr")
    if(len(abstract)!=0):
        a = abstract[0].p
        print(i,a)
        scrape.append(abstract)
