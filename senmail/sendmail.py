#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
sender = 'weihuan_cs@163.com'
# receivers = ['whutweihuan@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
receivers = 'whutweihuan@163.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('6级考试，操作系统考试，安卓开发，体系结构报告，爬虫报告', 'plain', 'utf-8')
# message['From'] = Header(sender, 'utf-8')   # 发送者
message['From'] = sender   # 发送者
message['To'] =  receivers		# 接收者
 
subject = 'task'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
	server = smtplib.SMTP('smtp.163.com',25)
	server.starttls()
	server.login(sender,'abc10086')
	server.sendmail(sender, receivers, message.as_string())
	print ("邮件发送成功")
	server.quit()
except smtplib.SMTPException:
	print ("Error: 无法发送邮件")