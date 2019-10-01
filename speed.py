import threading
import csv
from bs4 import BeautifulSoup
from requests import get
from tqdm import tqdm
def mine_paper(num,count):
    a = []
    scrape = [["S.no","PMID","Title","Abstract"]]
    url = ""
    cnt = 1
    file='res.csv'
    for i in tqdm(range(num,num+1000)):
        response = get(url+str(i))
        html_soup = BeautifulSoup(response.text,'html.parser')
        abstract = html_soup.find_all('div',class_="abstr")
        title = html_soup.find_all('div',class_="rprt abstract")
        if(len(abstract)!=0 and len(title)!=0):
            a = abstract[0].p
            b = title[0].h1
            scrape.append([cnt,i,b,a])
            cnt+=1
            result = open(file+str(count),'w',newline="")
            wr = csv.writer(result)
            wr.writerows(scrape)
if __name__ == "__main__":

    t1=threading.Thread(target=mine_paper, args=(3000000,1))
    t2=threading.Thread(target=mine_paper, args=(3100000,2))
    t3=threading.Thread(target=mine_paper, args=(3200000,3))
    t4=threading.Thread(target=mine_paper, args=(3300000,4))
    t5=threading.Thread(target=mine_paper, args=(3400000,5))
    t6=threading.Thread(target=mine_paper, args=(3500000,6))
    t7=threading.Thread(target=mine_paper, args=(3600000,7))
    t8=threading.Thread(target=mine_paper, args=(3700000,8))
    t9=threading.Thread(target=mine_paper, args=(3800000,9))
    t10=threading.Thread(target=mine_paper, args=(3900000,10))    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()    
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()