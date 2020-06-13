import gzip
import json

zip_file = 'jawiki-country.json.gz'

# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
print('20.')


def extract_UK():
    with gzip.open(zip_file, 'rt', encoding='utf-8', newline='') as file:
        for line in file:
            json_data = json.loads(line)
            if 'イギリス' in json_data['title']:
                return json_data['text']


# 記事中でカテゴリ名を宣言している行を抽出せよ．
print('21.')
import re

pattern = re.compile('^(\[\[Category.*)$', re.MULTILINE)
result = re.findall(pattern, extract_UK())
for i in result:
    print(i)

# new_data = extract_UK().split('\n')
# for line in new_data:
#     if 'category' in line.lower():
#         print(line)

# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
print('22.')

pattern = re.compile(r'''
                    ^ # 行頭
                    \[\[Category: # [[Category: は除外
                    ( # グループ開始
                    .*? # 非貪欲
                    ) # グループ終了
                    (?: # 対象外グループ開始
                    \|.* # |以降の文字を除外
                    )? # 対象外グループ終了
                    \]\] # \]\] は除外
                    .* # \]\]に続く文字も全て除外
                    $
                    ''', re.MULTILINE + re.VERBOSE)
# r'^\[\[Category:(.*?)(?:\|.*)?\]\].*$
result = re.findall(pattern, extract_UK())
for i in result:
    print(i)

# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
print('23.')

pattern = re.compile(r'''
                    ^ # 行頭
                    (={2,}) # キャプチャ対象：2個以上の=
                    \s* # 0個以上の空白を除去
                    (.*?) # キャプチャ対象：記号除く文字列
                    \s* # 0個以上の空白を除去
                    \1 # 後方参照、一つ目のキャプチャ対象と同じものを指定
                    .* # 任意の文字列
                    $ # 行末
                    ''', re.MULTILINE + re.VERBOSE)
# 1行で書くと、↓
# pattern = re.compile(r'^(={2,})\s*(.*?)\s*\1.*$', re.MULTILINE)
result = re.findall(pattern, extract_UK())
print(result)
for line in result:
    level = len(line[0]) - 1
    print('{indent}{section}({level})'.format(
        indent='\t' * (level - 1),
        section=line[1],
        level=level
    ))

# 記事から参照されているメディアファイルをすべて抜き出せ．
print('24.')

pattern = re.compile(r'^ファイル:(.*?)\|.*$', re.MULTILINE)
result = re.findall(pattern, extract_UK())
for i in result:
    print(i)

# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
print('25.')

pattern = re.compile(r'^{{基礎情報.*?$(.*?)}}$', re.MULTILINE + re.DOTALL)
contents = re.findall(pattern, extract_UK())

pattern = re.compile(r'''^
                     \|
                     (.*?)
                     \s*=\s*
                     (.*?)
                     (?:
                       (?=\n\|)
                       |
                       (?=\n$))
                     ''', re.MULTILINE + re.VERBOSE + re.DOTALL)
result = re.findall(pattern, contents[0])
result2 = pattern.findall(contents[0])
dic_contents = {}
for i in result:
    dic_contents[i[0]] = i[1]

for key, value in dic_contents.items():
    print(key)
    print('\t' + value)

# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
print('26.')

pattern = re.compile(r'^{{基礎情報.*?$(.*?)}}$', re.MULTILINE + re.DOTALL)
contents = re.findall(pattern, extract_UK())

pattern = re.compile(r'''^
                     \|
                     (.*?)
                     \s*=\s*
                     (.*?)
                     (?:
                       (?=\n\|)
                       |
                       (?=\n$))
                     ''', re.MULTILINE + re.VERBOSE + re.DOTALL)
result = re.findall(pattern, contents[0])

for key, value in result:
    if "'" in value:
        w = re.sub(r'\'{2,5}', '', value)
        print(key + ':' + w)
    else:
        print(key + ':' + '\t' + value)

# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
print('27.')

def templates():
    '''
    記事に含まれる「イギリス」から「基礎情報」のフィールド名と値を抜き出し
    returnでresultを返す
    '''
    pattern = re.compile(r'^{{基礎情報.*?$(.*?)}}$', re.MULTILINE + re.DOTALL)
    contents = re.findall(pattern, extract_UK())

    # with open('test.csv', 'w', encoding='utf-8', newline='') as file:
    #     file.writelines(contents)

    pattern = re.compile(r'''^
                         \|
                         (.*?)
                         \s*=\s*
                         (.*?)
                         (?:
                        (?=\n\|)
                        |
                        (?=\n$))
                        ''', re.MULTILINE + re.VERBOSE + re.DOTALL)
    fields = re.findall(pattern, contents[0])
    return fields

result = templates()
for key, value in result:
    if "'" in value:
        w = re.sub(r'\'{2,5}', '', value)
        # print(key + ':' + '\t' + w)
        print(w)
    elif "[[" in value:
        w2 = re.sub(r'\[{2}|\]{2}', '', value)
        # print(key + ':' + '\t' + w2)
        print(w2)
    else:
        # print(key + ':' + '\t' + value)
        print(value)

# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
print('28.')

fields = templates()

def remove_markup(target):
    # 強調マークアップ削除
    target = re.sub(r'\'{2,5}', '', target)
    # 内部リンクマークアップ削除
    target = re.sub(r'\[{2}|\]{2}', '', target)
    # 外部リンクマークアップ削除
    target = re.sub(r'\[http://.*?\]', '', target)
    # Template:Langの除去        {{lang|言語タグ|文字列}}
    target = re.sub(r'[\*{1,2}{{|{{].*?\|.*?}}', '', target)
    # <br>、<ref>の除去
    target = re.sub(r'<\/?[br|ref]\s?\/>', '', target)
    return target

result = {}
for field in fields:
    result[field[0]] = remove_markup(field[1])

for key, value in result.items():
    print(value)