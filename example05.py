#实例：中国大学排名定向爬虫；#这里没有拿到排名的名词，因为标签嵌套出现问题，暂时获取不到排名的那个标签；

import requests
import bs4
from bs4 import BeautifulSoup

#从网络上获取大学排名网页内容：
def getHTMLText(url):
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return print("爬取信息失败")




#提取网页内容中信息到合适的数据结构：
def fillUnivList(ulist, html):
	soup = BeautifulSoup(html, "html.parser")
	for tr in soup.find('tbody').children:
		if isinstance(tr, bs4.element.Tag):
			tds = tr('td') #找出tr里边的所有td
			ulist.append([tds[1].string, tds[3].string])




#利用数据结构展示并输出结果：
def printUnivList(ulist, num):
	print("{:^10}\t{:^10}".format("学校名称", "总分"))
	for i in range(num):
		u = ulist[i]
		print("{:^10}\t{:^10}".format(u[0], u[1]))




#主要代码
def main(num):
	uinfo = []
	url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html"
	html = getHTMLText(url)
	fillUnivList(uinfo, html)
	printUnivList(uinfo, num)

