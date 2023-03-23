import requests,json,bs4
from bs4 import BeautifulSoup as parser
ses=requests.Session()

def main():
	dev = input(" masukan device : ").lower()
	if dev in["iphone","ipad","ios"]:
		url = f"https://whatmyuseragent.com/brand/ap/apple"
		scrape_apple(url,dev)
	else:
		url = f"https://whatmyuseragent.com/brand/{dev[:2]}/{dev}"
		scrape_android(url)

def scrape_android(url):
	data = parser(ses.get(url).text,"html.parser")
	for z in data.find_all("a",{"href":True,"class":False}):
		get = parser(ses.get("https://whatmyuseragent.com"+z["href"]).text,"html.parser")
		for x in get.find_all("td",{"class":"useragent"}):
			print(x.text)
				
def scrape_apple(url,dev):
	data = parser(ses.get(url).text,"html.parser")
	for z in data.find_all("a",{"href":True,"class":False}):
		if dev in z.text.lower():
			get = parser(ses.get("https://whatmyuseragent.com"+z["href"]).text,"html.parser")
			for x in get.find_all("td",{"class":"useragent"}):
				print(x.text)
				
main()
