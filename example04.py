#爬取图片；
import requests
import os

def getImage(url):
	root = "E://googleDownload//"
	path = root + url.split("/")[-1]
	kv = {"user-agent": "Mozilla/5.0"}
	try:
		if not os.path.exists(root):
			os.mkdir(root)
		if not os.path.exists(path):
			r = requests.get(url, headers=kv, timeout=30)
			with open(path, "wb") as f:
				f.write(r.content)
				print("文件保存成功！")
		else:
			print("文件已经存在")
	except:
		return print("爬取失败！")
