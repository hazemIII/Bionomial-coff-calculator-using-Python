'''
Created on Nov 8, 2014

@author: hazem
'''
from math import factorial
n=input('enter n ')
k=input('enter K')
def BC_direct(n,k):
    if k < 0 or k > n:
        print('error')
        return 0;
    factn=factorial(n)
    factK=factorial(k)
    factm=factorial(n-k)
    print('direct is')
    print(factn/factK/factm)
    
BC_direct(n, k)