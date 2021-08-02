# %%
with open('./oz_cleaned.md','r') as file:
    text = file.read()

# テキストの単語への分割
words = text.split()

# 各単語の出現回数を格納した辞書の作成
# Pythonっぽいやり方
count = {w:words.count(w) for w in set(words)}

# 泥臭いやり方
'''
count = dict()

for w in words:
    if w in count.keys():
        count[w] += 1
    else:
        count[w] = 1
'''

# 出力する行のリスト(まずは最初の3行)
output_lines = ['# Word frequencies in chapter 1\n\n',
'|word|count|\n','|--|--|\n']

# 出力する行のリストに足していく
# 内包表記でもできるがforループのほうが見やすいかも
for key in sorted(count.keys()):
    output_lines.append('|'+key+'|'+str(count[key])+'|\n')

with open('./word_count.md','w') as file:
    file.writelines(output_lines)

# %%
