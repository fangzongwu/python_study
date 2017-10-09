### 爬取国家地理中文网首页的图片信息；
import requests
import bs4
from bs4 import BeautifulSoup


#获取网页内容信息
def getHTMLImage(url):
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return print("爬取信息失败")



#提取网页信息到适合的数据结构
def fillImageList(ulist, html):
	soup = BeautifulSoup(html, "html.parser")
	for tr in soup.find_all('img', height='150'):
		if isinstance(tr, bs4.element.Tag):
			ulist.append(tr.attrs['src'])
			print(ulist)




#利用数据结构展示并输出结果
def printImageList():
	pass



#主要代码
def main():
	imageList = []
	url = 'http://www.nationalgeographic.com.cn/'
	html = getHTMLImage(url)
	fillImageList(imageList, html)




