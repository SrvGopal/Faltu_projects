from random import *

lst = []
keys = "1234567890~!@#$%^&*()_+-`={}|[ABCDEGFHIJKLMNOPQRSTUVWXYZ]:;,/<>?.qwertyuiopasdfghjklzxcvbnm"

for i in keys:
    lst.append(i)

size = int(input("Enter the length of your password "))
password =""
length = len(lst)

for i in range(size+1):
    index = randint(0,length)
    char = lst[index]
    password = password+char

print(password)








