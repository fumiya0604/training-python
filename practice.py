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
# name = {'石田':'光成','織田':'信長','柴田':'勝家'}
# print(name)
# print(name['石田'])
# print(name['柴田'])
# # 要素の追加・変更・削除
# name ['豊臣'] = '秀吉'  #キーがすでにない場合はディクショナリに追加される
# name ['織田'] = '信成'  #キーがすでにある場合はディクショナリに変更される
# print(name)
# # 削除する場合は最初にdelをつけ削除したい要素のキーを入れる
# del name ['豊臣']
# print(name)

# # タプルとセット
# # タプルは()で定義するが要素の追加・変更・削除はできない
# # タプルは追加・変更・削除ができないため書き換える必要のないデータを管理また書き換えられていないことを保証できる
# aaa = ('yoru','shimo')
# bbb = (300,55,45,100)
# print(aaa)
# print('要素数は{}'.format(len(aaa)))
# print('合計は{}'.format(sum(bbb)))
# print(type(aaa))　#print(type)でしっかりtupleになっているか確認
# print(type(bbb))
# セットは重複せず順序もなくキーや添え字もない　appendの代わりにaddを使って要素の追加を行う
# セットは種類の管理に向いている

# 条件分岐　if else elif true false

# if文
# clase_tal = int(50+63+71+66+59+47+31+73+87+90)
# print(clase_tal)
# scor_target = int(input('目標点数を入力してください>>'))
# scor_res    = int(input('結果の点数を入力してください>>'))
# clase_avg   = int((clase_tal+scor_res)/11)
# print(clase_avg)

# if scor_res < 0 or scor_res > 100:
#     print('異常な点数です')
#     print('入力し直してください')
# elif scor_res >= 40:
#     print('赤点回避おめでとう！')
#     if clase_avg <= scor_res:
#         print('クラス平均より高いですね！')
# else:
#     print('残念ながら赤点です')
#     print('補習を受けてください')  

# while文
# count = 0
# while count < 20:
#     count += 1
#     print('羊が{}匹'.format(count))
# print('おやすみなさい')

# is_awake = true
# count = 0
# while is_awake == true:
#     count += 1
#     print('羊が{}匹'.format(count))
#     key = input('もう眠りそうですか？(y/n)>>')
#     if key == 'y':
#         is_awake = false
# print('おやすみなさい')
# if clase_avg < scor_res:
#     print('よく頑張りました')
# else:
#     clase_avg > scor_res
#     print('もっと頑張りましょう')

# count = 0
# student_num = int(input('学生の数を入力>>'))
# score_list = list()
# while count < student_num:
#     count += 1
#     score = int(input('{}人目の得点を入力>>'.format(count)))
#     score_list.append(score)
# print(score_list)
# total = sum(score_list)
# print('平均点は{}です'.format(total/student_num))

scores = [50,20,60,80,96]
# count = 0
# while count < len(scores):
#     if scores[count] >= 60:
#         print('OK')
#     else:
#         print('NO')
#     count += 1

# 繰り返しを使ったリストの参照のやり方
# カウンタ変数　= 0
# while カウンタ変数 < len(リスト):
#   リスト[カウンタ変数]を使った処理
#   カウンタ変数 += 1

# print('すべての質問にyまたはnで答えてください')
# okane_aruka = input('お金に余裕はあるか>>')
# if okane_aruka == 'y':
#     onaka_suiteruka = input('お腹が空いているか>>')
#     nomitai_kibun = input('ビール飲みたい？>>')
#     if onaka_suiteruka == 'y' and nomitai_kibun == 'y':
#         print('焼肉はいかが？')
#     elif onaka_suiteruka == 'y':
#         print('カレーはいかが？')
#     elif nomitai_kibun == 'y':
#         print('焼き鳥はいかが？')
#     else:
#         print('パスタはいかが？')
#     yashoku_iruka = input('夜食は必要？>>')
#     if yashoku_iruka == 'y':
#         print('コンビニチキンはいかが？')
# else:
#     print('家で食べましょう')

# for文　繰り返し
for data in scores:
    if data >= 60:
        print('OK')
    else:
        print('NO')

# # for文でリストの全要素を参照す
# for 変数　in リスト:
#     繰り返し処理

for x in range(3):
    print(10*2)

# range関数　決まった回数ループを回す
# for 変数 in range(回したい回数):
#     繰り返し処理

# while文とfor文の使い分け
# while文・繰り返す回数の目処が立たないときに使う
# for　文・繰り返す回数の目処が立つときに使う

# 繰り返しの制御
ages = [10,20,23,25,28,51,77,8,3,30]
num = 5
samples = list()
for age in ages:
    if 24 <= age <= 30:
        if len(samples) < num:
            samples.append(age)
print(samples)

sample = list()
for data in ages:
    if 0 <= data < 30:
        sample.append(data)
        if len(sample) == num:
            break
print(sample)

agess = [10,20,23,25,'ひみつ',28,51,77,8,3,30,'無回答']
samp = list()
for data in agess:
    if not isinstance(data,int):
        continue
    if data < 20 or data >= 30:
        continue
    samp.append(data)
print(samp)


