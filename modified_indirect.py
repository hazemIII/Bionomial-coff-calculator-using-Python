'''
Created on Nov 8, 2014

@author: hazem
'''
n=input('enter n ')
k=input('enter K')
def BC_modified_indirect(n,k):
    if k < 0 or k > n:
        print('error')
        return 0;
    bc=1
    for i in range(0,k):
        bc*=(n-i)
        bc/=(i+1)
    print(bc)
BC_modified_indirect(n, k)
    