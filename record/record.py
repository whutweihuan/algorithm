#coding=utf8
import xlrd

workbook = xlrd.open_workbook('record.xlsx')
sheetbook = workbook.sheets()[0]

isBixiu = sheetbook.col_values(4)[1:] #必修课
xuefen = sheetbook.col_values(5)[1:]  #学分
jidian = sheetbook.col_values(9)[1:] #成绩

# if str1.find(str2)>=0:
# 包含的话，返回第一次出现的位置，没有的话为负数

xuefen_sum = 0 
jidian_sum = 0;
for i in range(len(isBixiu)):

	if isBixiu[i].find('选修')>=0  or isBixiu[i].find('公选')>=0 or isBixiu[i].find('个性')>=0:
		continue;
	print (isBixiu[i])
	xuefen_sum += xuefen[i]
	jidian_sum += jidian[i] * xuefen[i];

print("平均学分绩点是{:.3f},必修课总学分是{}".format(jidian_sum/xuefen_sum,xuefen_sum))






