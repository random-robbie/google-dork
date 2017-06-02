from google import search
import os
import requests

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



dork = grab_dork ()
print ("Dork Being Used..... "+dork+"")
out=open("results.txt","a")
try:
	for title in search(""+dork+" &", stop=100):
				print(title)
				out.write(title)
				out.write("\n")
	out.close()
except:
		print ("Google Capture.. Urgh")
