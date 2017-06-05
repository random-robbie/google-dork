from google import search
import os
import requests
import argparse

### Config ###
proxy = "http://127.0.0.1:8080"
os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy
fo = open(".google-cookie", "w")
fo.close()


def grab_dork ():
	session = requests.Session()
	paramsGet = {"script":"test"}
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0","Connection":"close","Accept-Language":"en-US,en;q=0.5","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Upgrade-Insecure-Requests":"1"}
	response = session.get("http://xsses.rocks/dork/api.php", params=paramsGet, headers=headers)
	return response.text


parser = argparse.ArgumentParser(description='Enter your Own Dork or Use System generated Dork')
parser.add_argument('-d', action='store', dest='dork',
                    help='type in your custom dork i.e inurl:&')


results = parser.parse_args()

if results.dork == None:
	dork = grab_dork ()
else:
	dork = results.dork
print ("Dork Being Used..... "+dork+"")
out=open("tocheck3.txt","a")
for title in search(""+dork+" &", stop=200):
	if title.startswith(("https://www.youtube.com","http://vk.com","https://www.linkedin.com","https://en.wikipedia.org","https://itunes.apple.com","https://www.github.com","https://twitter.com","https://github.com","https://stackoverflow.com","https://www.facebook.com")):
		print (""+title+"... Ignored")
	elif title.endswith((".pdf",".txt","sitemap.xml")):
		print (""+title+"... Ignored")
	else:
		print(title)
		out.write(title)
		out.write("\n")

		
out.close()

