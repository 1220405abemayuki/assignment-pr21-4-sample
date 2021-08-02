# %%
with open('./oz_cleaned.md','r') as file:
    text = file.read()

words = text.split()
count = dict()

for w in words:
    if w in count.keys():
        count[w] += 1
    else:
        count[w] = 1

keys = list(count.keys())
keys.sort()

output_lines = ['# Word frequencies in chapter 1\n\n',
'|word|count|\n','|--|--|\n']

for key in keys:
    output_lines.append('|'+key+'|'+str(count[key])+'|\n')

with open('./word_count.md','w') as file:
    file.writelines(output_lines)
