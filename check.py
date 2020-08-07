import urllib.request
import urllib.error
import time
from multiprocessing import Pool
import requests
start = time.time()

file = open('missing_2.txt', 'r', encoding="ISO-8859-1")
urls = file.readlines()

#print(urls)


def checkurl(url):
    try:
        resp = requests.get(url)
        print(resp.status_code,url)
    except Exception as ex:
        print("Except")
        print(str(ex),url)

if __name__ == "__main__":
    p = Pool(processes=20)
    result = p.map(checkurl, urls)

print("done in : ", time.time()-start)

