import re
from urllib import request
import urllib
import os

# make dir
mypath = "D:\\PIC\\29\\"

if not os.path.exists(mypath):
	os.mkdir(mypath)
	print ("创建文件夹成功！")
else:
	print("文件夹已经存在！")

# url = "http://www.baidu.com"
url = "http://www.ruanyifeng.com/blog/2018/11/weekly-issue-29.html"
# url = "http://www.ruanyifeng.com/blog/2018/11/weekly-issue-31.html"

# Get source
source = request.urlopen(url).read().decode('utf-8');
# print(source)

# Set match pattern
pattern = re.compile("<img src=\"https://www.wangbase.com/blogimg/asset/.*?\.jpg\"",re.S)

items = re.findall(pattern,source)


i  = 0;
for item in items:
	try:
		print("正在爬取:\t" + item[10:-1])
		picture = request.urlopen(item[10:-1])
		picname = mypath+str(i)+".png";
		i+=1;
		if not os.path.exists(picname):
			f = open(picname,'wb')
			f.write(picture.read())
		else:
			print("图片已经存在")
	except :
		print("没有图片")
print("完成！")


