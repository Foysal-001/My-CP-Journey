# -*- coding: utf-8 -*-
"""problem_705A.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_gl3E8iOkwVt9NilhSV0uLm8fRaHyRgy
"""

n =int(input())
i=1
strn =''
while(i<=n):

    if n==1:
        strn +='I hate it'
    elif n!=1 and i%2!=0 and i==1 :
        strn +='I hate that '
    elif n!=1 and i%2!=0 and i!=n:
        strn +='I hate that '
    elif n!=1 and i%2!=0 and i ==n:
        strn +='I hate it '
    elif n!=1 and i%2==0 and i==n:
        strn +='I love it'
    elif n!=1 and i%2==0 and i!=n:
        strn +='I love that '

    i +=1
print(strn)