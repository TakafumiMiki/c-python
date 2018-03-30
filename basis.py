import random
b = 0   #これがないとエラーになる
for i in range(10000):
    rand = random.random()*101 #101のとき 0~100
    if int(rand) == 100: 
        b+=1
print(b)   #100%表記の乱数


"""
print(2**5) #2^5 との違い

a = [114, 514, 187, 810]

print (len(a))  #4
print (a[2])    #187 a[0] == 114
print (810 in a)    #True

b = sorted(a)
print ("a = {0} \nb = {1}".format(a,b)) #a = [114, 514, 187, 810] b = [114, 187, 514, 810]

a.sort()
print (a)   #[114, 187, 514, 810]

a.reverse()
print (a)   #[810, 514, 187, 114]
"""
"""
for i in range(1, 101): #1から100まで
    if i % 17 == 0:
        print(i)

for i in range(6,10): #6から9まで
    if i % 2 == 0:
        print("偶数",i)
    else:
        print("奇数",i)
"""
"""
name = "iwana"  #変数の有効範囲
def hello():    
    name = "cooky"
    print (name)
hello() #cooky
print(name) #iwana
"""

