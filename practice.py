# 1----変数・データ型
# print('1'+'1')
# #これは文字列の'1'と'1'を足しているだけだから出力で「11」と表示される
# print(1+1)
# #これは整数の1+1をしているため出力で「2」と表示される

# # 2----データ型種類
# # int    整数  　100
# # float  少数　　10.0
# # str    文字列　"hello"、"こんにちは"
# # bool   真偽値　true、false

# # 3----変数
# a = (10)
# print(a)
# b = ("これは文字列です")
# print(b)
# x,y = ("文字列",10)
# print(x,y,a,b)
# age = (24)
# age = (age+1)
# age += 1        #代入演算子　・+=　・-=　・*=　・/=
# print(age)

# #input関数,format関数
# name = input('あなたの名前を教えてください>>')
# print('私の名前は{}で、年齢は{}歳です'.format(name,age))

# 2---コレクション

# リスト　　要素は０番から始まる
# name = ['a','b,','c','d',100]
# age  = [10,15,20,25]
# # 様々な要素を入れることができる、要素は０からとなっている
# scores = [100,88,97.68]
# total = sum(scores)
# avg = total / len(scores)      #len関数はリストの中の要素を数える
# print('合計{}点で、平均{}点'.format(total,avg))
# # リストに要素の追加、削除、変更
# name.append('e')  #リスト名.appendでそのリストに要素を追加できる
# print(name)
# name.remove('e')  #リスト名.removeでそのリストの要素を削除できる
# print(name)
# name[4] = 'e'     #リスト名[変更したい要素の番号] = 変更後の要素
# print(name)

# ディクショナリ　　要素に対してキーを持っている
# 変数 = {キー1:値,キー2:値,キー3:値・・・}
name = {'石田':'光成','織田':'信長','柴田':'勝家'}
print(name)
print(name['石田'])
print(name['柴田'])
# 要素の追加・変更・削除
name ['豊臣'] = '秀吉'  #キーがすでにない場合はディクショナリに追加される
name ['織田'] = '信成'  #キーがすでにある場合はディクショナリに変更される
print(name)
# 削除する場合は最初にdelをつけ削除したい要素のキーを入れる
del name ['豊臣']
print(name)

# タプルとセット
# タプルは()で定義するが要素の追加・変更・削除はできない
# タプルは追加・変更・削除ができないため書き換える必要のないデータを管理また書き換えられていないことを保証できる
aaa = ('yoru','shimo')
bbb = (300,55,45,100)
print(aaa)
print('要素数は{}'.format(len(aaa)))
print('合計は{}'.format(sum(bbb)))
print(type(aaa))　#print(type)でしっかりtupleになっているか確認
print(type(bbb))
# セットは重複せず順序もなくキーや添え字もない　appendの代わりにaddを使って要素の追加を行う
# セットは種類の管理に向いている

