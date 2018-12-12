/***********************************************
#
#        Author: weihuan -whutweihuan@163.com
#        Create: 2018-11-19 
# Last Modified: 2018-11-19 
#          Link: 
#   Description: 子数组最大值

***********************************************/

#include<iostream>


using namespace std;

int sumsub(int a[],int n){
    int cur =0;
    int max =  1<<31 ;
    int sum = 0;
    while(cur<n){
        sum += a[cur++];
        if(sum>max){
            max = sum;
        }else if(sum<0){
            sum=0;
        }
    }
    return sum;
}

int main(){
    int a[] = {1,2,3,4,-100,99,3};
    int n = sizeof(a)/sizeof(a[0]);
    cout<<sumsub(a,n)<<endl;
    
    
    
}