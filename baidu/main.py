import re
from urllib import request
import urllib
import os



# url = "http://www.baidu.com"
keyword = "tree2"
url = "http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1543645909193_R&pv=&ic=0&nc=1&z=0&hd=0&latest=0&copyright=0&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=" + keyword 
# url = "http://www.ruanyifeng.com/blog/2018/11/weekly-issue-31.html"
print(url)

# make dir
mypath = "D:\\PIC\\"+keyword+"\\"

if not os.path.exists(mypath):
	os.mkdir(mypath)
	print ("创建文件夹成功！")
else:
	print("文件夹已经存在！")

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    "cookie":"_zap=b290dd20-a85f-44c5-af6b-aa28848f006e; _xsrf=F3U3FTn4rOhfuUODMVhoiNtaDzEKBPLL; d_c0=\"ABAncL3kWA6PToRX53pc_r372dLYBA5Uv8c=|1539263711\"; __utma=51854390.383630342.1539591899.1539591899.1539591899.1; __utmz=51854390.1539591899.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/wei-jian-feng-89/activities; __utmv=51854390.100--|2=registration_date=20180314=1^3=entry_date=20180314=1; q_c1=b02f09f6d2a34f2fabbd760a751ff42e|1542214972000|1539263763000; capsion_ticket=\"2|1:0|10:1543280884|14:capsion_ticket|44:NTUwZjY1ZTZjZGEyNDBiZDhhMzkwZjQ4NDhkNzhiNWY=|27e63993f9b0811713ea94de8c6e4821b34034351155e21ca5664ffb7a213b0e\"; z_c0=\"2|1:0|10:1543280893|4:z_c0|92:Mi4xSVg4eENBQUFBQUFBRUNkd3ZlUllEaVlBQUFCZ0FsVk5fZWJwWEFERUMwa0NzU3U0UHlEY0JyajdyMXkwOGp2REtB|45ba9b49989a1b89a7700bd95b5b5b7661d31d4273ed453b828c227ff42db3a8\"; tst=h; tgw_l7_route=c919f0a0115842464094a26115457122"
    }



# Get source
req = request.Request(url=url,headers = headers)
source = request.urlopen(url).read().decode('utf-8')
# print(source)

# Set match pattern
pattern = re.compile("\"thumbURL\":\"https?:\/\/.*?\.jpg\"",re.S)

items = re.findall(pattern,source)
# print(items)

i  = 0;
for item in items:
	try:
		print("正在爬取:\t" + item[12:-1])
		picture = request.urlopen(item[12:-1])
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


