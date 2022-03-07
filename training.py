print("hello world")

# for i in range(40):
#     num = i+1
#     if num%4==0 and "2" in str(num):
#         print("wao!")
#         continue
#     if num%3==0 and "3" in str(num):
#         print("aho")
#     else:
#         print(num)


# for i in range(0,100,5):
#     num = i+1
#     if "1"in str(num):
#         print("zero")
#     if "10"in str(num):
#         print("tenten")
#     else:
#         print(num)


# def add(x,y,z,r):
#     return x*y+(x+z*r)

# res = add(5,2,5,2)
# print(res)

# def add(x,y,z):
#     return (x*y)/2

# for i in range(100):
#     num = i+1
#     if num % (i+1) ==0:
#     print(num)

# l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']

# print(l.count('a'))
# # 4

# print(l.count('b'))
# # 1

# print(l.count('c'))
# # 2

# print(l.count('d'))
# # 0

# for i in range(10):
#     num = i+1
#     for j in range (1):
#         if num % (2) ==0:
#             print(num)

# add = lambda x,y,z: (((x+y)*z)/2)

# res = add(5,2,3)
# print(res)

# for i in range(0,1000):
#     if i % 2 == 0:
#      if i % 5 == 0:
#       if i % 9 == 0:
#           if i % 13 == 0:
#                     print(i)
    # else: i % 3 == 2
    # print(i)

# a = 5
# b = 3
# ans = "{}%{}={}".format(a, b, a%b)
# print(ans)

# list1 = [for i in range(100)]
#     if i%2 == 0:
#         if i%5 == 0:
#             print(len(i))
# list1_sorted_len = sorted(l, key=len)
# print(list1_sorted_len)

# list1 = []
# add = lambda 
# print(add)

 
# print( "リストの初期化" )
var_list=[1,2,3,4,5]
print( var_list )
 
# print( "異なる型が混合したリスト" )
var_list2=['a','abd',3,0.1,'a']
print( var_list2 )
 
# print("要素の指定")
print( var_list2[1])
print( var_list2[-1])
 
# print( "リストへ要素の追加")
var_list2.append( 'item1')
print( var_list )
 
# print( "リストから要素の削除")
 
# print( "最初の要素を削除")
del var_list2[0]
print( var_list2 )
 
# print( "最後の要素を削除")
del var_list2[-1]
print( var_list2 )
 
# print( "リストのソート")
var_list3=['d','g','a','x','1']
sortedlist=sorted(var_list3)
print( var_list3)
print( sortedlist )
 
# print("リストを文字列に変換" )
joinlist=','.join(sortedlist)
print( joinlist )
 
# print("文字列をリストに変換")
var_list4='a,b,c,d,e,f,g'
splitlist=var_list4.split(',')
print( splitlist )