#print("hello world!!")

num = 1
#print(num)

#mozi = "おはよう"
#print(mozi)

#isok = True
#isok = False
#if isok:
#    print("ok")
#elif num<10:
#    print("good")
#else:
#    print("ng")

#for i in range(10):
    #print(i)

for i in range(10):
    num = i+1
    tmp = []
    for j in range (num):
        if num % (j+1) ==0:
            tmp.append(num)
            print(tmp)
    if len(tmp) == 2:
        print(num)



# for i in range(40):
#     num = i+1
#     if num%3==0 or num%4==0 or "3" in str(num):
#         print("aho")
#     else:
#          print(num)

# def add(x,y):
#     return x+y


# res = add(3,5)
# print(res)

# rig = add(12,8)
# print(rig)

# nn = "abcdefg"
# print(nn.replace('a','b'))


# print(type('string') is int)
# print(type('string') is str)

# よくでてくる注意
# ci=pushしたときに自動でテストしてくれる
# cd=commitしたときに自動でDEPURPI(サ−バ−側)してくれる

# def is_str(v):
#     return type(v) in (str,int)

# print(is_str('string'))

# print(is_str(100))

# print(is_str([0, 1, 2]))

# print(type(True))

# print(type(False))