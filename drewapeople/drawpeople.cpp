/***********************************************
#
#        Author: weihuan -whutweihuan@163.com
#        Create: 2018-12-5 
# Last Modified: 2018-12-5 
#          Link: 
#         title:
#   Description: ---

***********************************************/

#include<iostream>
#include<cmath>
using namespace std;

int main(){
	int height = 20;
	for(int i=0;i<height;i++){
		for(int j=0;j<=height-1-i;j++){
			cout<<" ";
		}
		for(int j=0;j<2*i-1;j++){
			cout<<"*";
		}
		cout<<endl;
	}
	for(int i=height-1;i>=0;i--){
		for(int j=0;j<height-1-i;j++){
			cout<<" ";
		}
		for(int j=2*i;j>=0;j--){
			cout<<"*";
		}
		cout<<endl;
	}
	getchar();
}