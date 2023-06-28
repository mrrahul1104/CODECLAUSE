#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
nums=['1','2','3','4','5','6','7','8','9','0']
symbol=['/','!','@','#','$','%','&','*','~']
password=[]
print("--------PASSWORD GENERATOR--------")
print("Enter the length of the password you want:",end="")
length=int(input())
if(length>=5):
    sym=int(input("Enter the no.of symbols you want in password:"))
    nu=int(input("Enter the no.of digits in your password:"))
    if(sym+nu>length):
        print("Sorry!No password can be generated")
    else:
        le=length-(nu+sym)
        for i in range(1,sym+1):
            password.append(random.choice(symbol))
        for j in range(1,nu+1):
            password.append(random.choice(nums))
        for k in range(1,le+1):
            password.append(random.choice(letters))
        random.shuffle(password)
        res=""
        for m in password:
            res+=m
        print("Here is your password:"+res)
else:
    print("Minimum 5 characters should be present!")

