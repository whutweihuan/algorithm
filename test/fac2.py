def fac( n):
    if n !=1:
        return  n * fac(n-1)
    else:
        return 1

n = 10;
print ("{}的阶乘是：{}".format(n,fac(n)))


print("wei huan is so cool !")