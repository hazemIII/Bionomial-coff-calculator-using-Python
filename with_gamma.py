'''
Created on Nov 8, 2014

@author: hazem
'''
from math import *
n=input('enter n ')
k=input('enter K')
def BC_with_gamma(n,k):
    if k < 0 or k > n:
        print('error')
        return 0;
    BC=exp(lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1))
    print(BC)
BC_with_gamma(n, k)