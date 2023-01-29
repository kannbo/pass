passkey=[1,2,3,4,5,6,7,8,9,0,]
key=[]
password=''
def set_pass(lists):
    for i in range(len(lists)):
        passkey.append(lists[i])
import random
set_pass('abcdefghijklmnopqrstuvwxyz01234567890123456789')

#print(passkey)
for i in range(8):
    key.append(passkey[random.randrange(1,len(passkey))])
for i in range(len(key)):
    password = f'{password}'+f'{key[i]}'
input("パスワードを生成しました。" +"\n"+"pass:"+ "\n" + "\t"+password) #a
