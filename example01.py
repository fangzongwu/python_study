#requests库的使用;
import requests

def getHTML(url):
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text[:3000]
	except:
		return print("出现异常!")


