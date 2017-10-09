#获取禁止爬取的网站的内容；
import requests

def getHTML(url):
	try:
		kv = {"user-agent": "Mozilla/5.0"}
		r = requests.get(url, headers=kv)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text[1000:2000]
	except:
		return print("爬取失败")