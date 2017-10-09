#百度关键词搜索；
import requests

def getHTML(url):
	try:
		kv = {"q": "NBA"}
		r = requests.get(url, params=kv, timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text[:5000]
	except:
		return print("爬取失败")