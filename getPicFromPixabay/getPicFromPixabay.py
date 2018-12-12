import re
import os
import requests
import urllib
import time


class Spider():

    def __init__(self):
        self.keyword = input('欢迎使用pixabay图片搜索下载器\n请输入搜索关键词(推荐输入英文)：') 
        self.siteURL = 'http://pixabay.com/zh/photos/?image_type=&cat=&min_width=&min_height=&q=' + str(
            self.keyword) + '&order=popular'

        # 获取详情页源码

    def getSource(self, url):
        headers = {
             "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
             "cookie" :"_ga=GA1.2.666375935.1540428904; is_human=1; csrftoken=AcrCZerpAe4R4GqpUl24p5JxWMjpGbNiDD1yINC5sZyzjUi10hvbRnRLXgoleSJH; g_rated=; _gid=GA1.2.1554784586.1543461617; _gat=1; sessionid=\"eyJfbGFuZ3VhZ2UiOiJ6aCIsImRsIjpbNDU5Mjk5LDQ1NTEyMCwyNjk1NTY5LDI0ODEzNDYsMzM3MjcyMF0sInRlc3Rjb29raWUiOiJ3b3JrZWQifQ:1gSDBR:Gj8Oxp2kUj6LXXzlGS3FYYduDEg\"; client_width=854" }

        result = requests.get(url= url,headers= headers).text
        return result

        # 获取图片页数

    def getPageNum(self):
        result = self.getSource(self.siteURL)
        pattern = re.compile('<input name="pagi.*?>.*?/ (.*?) .*?', re.S)
        items = re.search(pattern, result)
        if items.group(1) >= str(1):
            print('\n这个关键词共有图片', items.group(1), '页')
        else:
            print('\n哎呀，木有您想要的图片呢。。。')
        return items.group(1)

        # 匹配正则1

    def getItem1(self, url):
        result = self.getSource(url)
        pattern1 = re.compile('<img srcset="https://cdn.pixabay.com/photo(.*?)-(.*?)__340.*?', re.S)
        items = re.findall(pattern1, result)
        return items

        # 匹配正则2

    def getItem2(self, url):
        result = self.getSource(url)
        pattern2 = re.compile('data-lazy-srcset="https://cdn.pixabay.com/photo(.*?)-(.*?)__340.*?', re.S)
        items = re.findall(pattern2, result)
        return items

        # 保存图片入文件

    def saveImage(self, detailURL, name):
        try:
            picture = urllib.request.urlopen(detailURL)
            fileName = name + '.jpg'
            string = 'D:\\Cloud\\%s\\%s' % (self.path, fileName)
            E = os.path.exists(string)
            if not E:
                f = open(string, 'wb')
                f.write(picture.read())
                f.close()
            else:
                print('图片已经存在，跳过！')
                return False
        except:
                print("图片不存在!")
                return False


    def makeDir(self, path):
        self.path = path.strip()
        E = os.path.exists(os.path.join('D:\\Cloud', self.path))
        if not E: 
            os.makedirs(os.path.join('D:\\Cloud', self.path))
            os.chdir(os.path.join('D:\\Cloud', self.path))
            print('成功创建名为', self.path, '的文件夹')
            return self.path
        else:
            print('名为', self.path, '的文件夹已经存在...')
            return False

            # 对一页的操作

    def saveOnePage(self, url):
        i = 1
        items = self.getItem1(url)
        for item in items:
            detailURL = 'https://cdn.pixabay.com/photo' + str(item[0]) + '-' + str(item[1]) + '_960_720.jpg'
            print('\n', '正在下载并保存图片', i, detailURL)
            self.saveImage(detailURL, name='Num' + str(i))
            time.sleep(0.5)
            i += 1
        if i > 16:
            items = self.getItem2(url)
            i = 17
            for item in items:
                detailURL = 'https://cdn.pixabay.com/photo' + str(item[0]) + '-' + str(item[1]) + '_960_720.jpg'
                print('\n', '正在下载并保存图片', i, detailURL)
                self.saveImage(detailURL, name='Num' + str(i))
                time.sleep(0.5)
                i += 1

                # 对多页图片的操作

    def saveMorePage(self):
        numbers = self.getPageNum()
        Num = int(input('一页共100张图，\n请输入要下载的页数(默认页数大于等于1）：'))
        Start = int(input('请输入下载起始页数：'))
        if numbers >= str(1):
            for page in range(Start, Start + Num):
                if page == 1:
                    print('\n', '正在获取第1页的内容......')
                    self.url1 = self.siteURL
                    self.makeDir(path=self.keyword + 'page' + str(page))
                    self.saveOnePage(url=self.url1)
                else:
                    print('\n', '正在获取第', page, '页的内容')
                    self.url2 = 'https://pixabay.com/zh/photos/?orientation=&image_type=&cat=&colors=&q=' + str(
                        self.keyword) + '&order=popular&pagi=' + str(page)
                    self.makeDir(path=self.keyword + 'page' + str(page))
                    self.saveOnePage(url=self.url2)
        else:
            return False
        
        print('\n', '所有图片下载成功！')

if __name__ == '__main__':
    spider = Spider()
    spider.saveMorePage()