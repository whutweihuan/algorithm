/*
用 vt码 
例：printf("\033[40;31m你要改变颜色的内容\033[0m"); 背景色为黑色，字体颜色位红色
只想要背景色printf("\033[40m你要改变颜色的内容\033[0m");
只想要自提颜色同上 改一下数字就行了 
背景色
40:黑
41:深红
42:绿
43:黄色
44:蓝色
45:紫色
46:深绿
47:白色
字体颜色:30-----------39
30:黑
31:红
32:绿
33:黄
34:蓝色
35:紫色
36:深绿
37:白色
*/
 
 
#include <stdio.h>
 
int main()
{
	printf("\033[44;37;5m *你要改变颜色的内容，黑底和红色字* \033[0m \n");
	printf("\033[47;32m *你要改变颜色的内容，白底和绿色字* \033[0m \n");
	printf("\033[43;35m *你要改变颜色的内容，黄底和紫色字* \033[0m \n");
	printf ("[0;31m *你要改变颜色的内容* [0;0m\n");
	return 0;
}