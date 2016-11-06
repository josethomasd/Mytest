#!/bin/python3

import sys

n = int(input().strip())
s = input().strip()
k = int(input().strip())


list1=list(s)
for i in range(0,n):
	if (ord(s[i])>=65 and ord(s[i])<=90):
		csum = ord(s[i])+k
		if csum>=90:
			msum=csum-91
			while (msum+65)>90:
				msum=(msum+65)-91
			list1[i]=chr(65+msum)
		else:
			list1[i]=chr(ord(s[i])+k)
	elif (ord(s[i])>=97 and ord(s[i])<=122):
		csum = ord(s[i])+k
		if csum>=122:
			msum=csum-123
			while (msum+97)>122:
				msum=(msum+97)-123
			list1[i]=chr(97+msum)
		else:
			list1[i]=chr(ord(s[i])+k)
	else:
		list1[i]=s[i]


print("".join(list1))