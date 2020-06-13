# 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
strings = 'stressed'
print('01.', strings[::-1])

# パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
word = 'パタトクカシーー'
print('')
print('02.', word[0::2])

# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，
# 各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ
words = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
words = words.rstrip('.')
words_list = words.split()

len_list = [len(i) for i in words_list]
print('')
print('03.', len_list)

# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
# それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ
words = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
words_list = words.split()
initials = {}
for i in range(1, len(words_list)+1):
    if i in [1, 5, 6, 7, 8, 9, 15, 19]:
        initial = words_list[i-1][0]
        initials[initial] = i
    else:
        initial = words_list[i-1][:2]
        initials[initial] = i
print('')
print('04.', initials)

# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
def n_gram(word, n):
    gram = [word[i:i + n] for i in range(len(word)-n + 1)]
    return gram


print('')
print('05.')
word = 'I am an NLPer'
s_result = n_gram(word, 2)
print(s_result)

words = word.split()
w_result = n_gram(words, 2)
print(w_result)

# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．


def bi_gram(word, n):
    bigram = [word[i:i + n] for i in range(len(word) - n + 1)]
    return bigram


print('')
print('06.')
word1 = 'paraparaparadise'
word2 = 'paragraph'

X = set(bi_gram(word1, 2))
Y = set(bi_gram(word2, 2))
print('和集合=', X | Y)
print('積集合=', X & Y)
print('差集合=', X - Y)
print('seがXに含まれるか=', 'se' in X)
print('seがYに含まれるか=', 'se' in Y)

# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．


def returns(x, y, z):
    return '{x}時の{y}は{z}'.format(x=x, y=y, z=z)


x, y, z = 12, '気温', 22.4
result = returns(x, y, z)
print('')
print('07.', result)

# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．


def cipher(word):
    result = ''
    for i in word:
        if i.islower():
            result += str(chr(219 - ord(i)))
        else:
            result += i
    return result


print('')
print('08.')
word = 'I am a Hero'
crypt_result = cipher(word)
print('暗号化=', crypt_result)

discrypt_result = cipher(crypt_result)
print('復号化', discrypt_result)

# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
# （例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，
# その実行結果を確認せよ．


def w_random(word):
    import random
    words = word.split()
    for i in range(len(words)):
        if len(words[i]) > 4:
            center = words[i][1:len(words[i]) - 1]
            random_word = ''.join(random.sample(center, len(center)))
            words[i] = words[i][0] + random_word + words[i][-1]
    return words


print('')
print('09.')
word = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
result = w_random(word)
result = ' '.join(result)
print(result)