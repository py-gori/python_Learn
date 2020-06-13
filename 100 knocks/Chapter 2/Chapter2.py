hightemp = 'hightemp.txt'
# 行数をカウントせよ．確認にはwcコマンドを用いよ．
with open('hightemp.txt', encoding='utf-8', newline='') as file:
    x = file.readlines()

print('10.', len(x))

# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
print('11.')
with open('hightemp.txt', encoding='utf-8', newline='') as file:
    x = file.read()
    print(x.replace('\t', ' '))

# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
print('12.')
with open(hightemp, encoding='utf-8', newline='') as file,\
    open('col1.txt', 'w', encoding='utf-8', newline='') as col1,\
    open('col2.txt', 'w', encoding='utf-8', newline='') as col2:
    for line in file:
        cols = line.split('\t')
        col1.write(cols[0] + '\r\n')
        col2.write(cols[1] + '\r\n')


# def write_txt(col_data, txtfile):
#     with open(txtfile, 'w', encoding='utf-8', newline='') as file:
#         file.write('\n'.join(col_data))
#
# col1 = []
# col2 = []
# with open('hightemp.txt', encoding='utf-8', newline='') as file:
#     while True:
#         x = file.readline()
#         if x:
#             l = x.split('\t')
#             col1.append(l[0])
#             col2.append(l[1])
#         elif not x:
#             break
#
# write_txt(col1, 'col1.txt')
# write_txt(col2, 'col2.txt')
#
# print('12.')
# with open('col1.txt', encoding='utf-8', newline='') as file:
#     x = file.read()
#     print(x)

# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
print('13.')
col1_l = []
col2_l = []
with open('col1.txt', encoding='utf-8', newline='') as col1,\
    open('col2.txt', encoding='utf-8', newline='') as col2,\
    open('output.txt', 'w', encoding='utf-8', newline='') as out:
    for _col1, _col2 in zip(col1, col2):
        out.write(_col1.rstrip() + '\t' + _col2.rstrip() + '\n')

# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ
print('14.')
N = int(input('整数を入力してください：'))

with open(hightemp, encoding='utf-8', newline='') as file:
    # reader = file.readlines()
    for i, line in enumerate(file):
        if i < N:
            print(line.rstrip())
        else:
            break

# for i in range(N):
#     print(reader[i].rstrip())

# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
print('15.')
N = int(input('整数を入力して下さい：'))

with open(hightemp, encoding='utf-8', newline='') as file:
    filedata = file.readlines()

# lines = len(filedata)
# get_line = lines - N
#
# for i in range(get_line, lines):
#     print(filedata[i].rstrip())

for line in filedata[-N:]:
    print(line.rstrip())

# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
print('16.')
import math
N = int(input('整数を入力してください：'))

with open(hightemp, encoding='utf-8', newline='') as file:
    filedata = file.readlines()

def write_data(filename, data):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(data)

# f_name = 'splitfile_'
# num = 1
count = len(filedata)
unit = math.ceil(count / N)

# for i in range(count):
#     if i == unit or i % unit == 0 and i != 0:
#         num += 1
#     write_data('{file}{n:02d}.txt'.format(file=f_name, n=num), filedata[i].rstrip() + '\n')

for i, offset in enumerate(range(0, len(filedata), unit), 1):
    with open('unit_{:02d}.txt'.format(i), 'w', encoding='utf-8', newline='') as file:
        # file.writelines(filedata[offset:offset + unit])
        for line in filedata[offset:offset+unit]:
            file.write(line)

# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
print('17.')

with open(hightemp, encoding='utf-8', newline='') as file:
    filedata = file.readlines()

set_todoufuken = set()
for line in filedata:
    cols = line.split('\t')
    set_todoufuken.add(cols[0])

print(set_todoufuken)

# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
print('18.')

with open(hightemp, encoding='utf-8', newline='') as file:
    filedata = file.readlines()

filedata = [i.split('\t') for i in filedata]
sort_filedata = sorted(filedata, key=lambda x: float(x[2]), reverse=True)

with open('sort.txt', 'w', encoding='utf-8', newline='') as file:
    for line in sort_filedata:
        file.writelines('\t'.join(line))

for line in sort_filedata:
    print('\t'.join(line).rstrip())

# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
print('19.')
# from itertools import groupby

with open(hightemp, encoding='utf-8', newline='') as file:
    filedata = file.readlines()

filedata = [i.split('\t') for i in filedata]

hightemp_dict = {}
for line in filedata:
    if line[0] not in hightemp_dict:
        hightemp_dict[line[0]] = 1
    else:
        hightemp_dict[line[0]] += 1

sort_todoufuken = sorted(hightemp_dict.items(), key=lambda x:x[1], reverse=True)

for todoufuken in sort_todoufuken:
    print("{}({})".format(todoufuken[0], todoufuken[1]))
