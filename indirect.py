'''
Created on Nov 8, 2014

@author: hazem
'''
from math import factorial
n=input('enter n ')
k=input('enter K')
def BC_indirect(n,k):
    if k < 0 or k > n:
        print('error')
        return 0;
    h=min(k,n-k)
    factm=factorial(h)
    f=1
    for i in range(0,(min(k,n-k))):
        f=f*(n-i)
    print('indirect is')
    print(f/factm)
BC_indirect(n, k)
        