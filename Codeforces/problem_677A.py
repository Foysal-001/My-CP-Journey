# -*- coding: utf-8 -*-
"""problem_677A.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XCuEAH9_CluemLqgcwEgsjA-UyKCYlaW
"""

x=str(input())
p=str(input())
a=[]
b=[]
count=0
b.extend(p.split(' '))
a.extend(x.split(' '))
if int(a[0])==len(b):
 for i in range(int(a[0])):
  if int(b[i])>int(a[1]):
    count+=2
  else:
    count+=1
 print(count)
else:
  pass