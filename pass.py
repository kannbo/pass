passkey=[1,2,3,4,5,6,7,8,9,0,]
key=[]#keyリスト
password=''#関数定義
def set_pass(lists):
    for i in range(len(lists)):
        passkey.append(lists[i])
import random #randomをインポート
set_pass('abcdefghijklmnopqrstuvwxyz01234567890123456789')#文字を追加

#print(passkey)
for i in range(8):#passkeyの文字でpass生成
    key.append(passkey[random.randrange(1,len(passkey))])
for i in range(len(key)):#変数に変換
    password = f'{password}'+f'{key[i]}'
input("パスワードを生成しました。" +"\n"+"pass:"+ "\n" + "\t"+password) #出力する
