'''
Created on Nov 8, 2014

@author: hazem
'''
n=input('enter n ')
k=input('enter K')
def binomialCoefficient(n, k):
    if k < 0 or k > n:
        return 0
    if k > n - k: # take advantage of symmetry
        k = n - k
    if k == 0 or n <= 1:
        return 1
    return binomialCoefficient(n-1, k) + binomialCoefficient(n-1, k-1)
print(binomialCoefficient(n, k))