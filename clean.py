# %%
with open('./oz.md','r') as file:
    text = file.read()

trans_rule = {'.':'',',':'','"':'',';':'','#':'',':':'','!':''}
trans = str.maketrans(trans_rule)
text_cleaned = text.translate(trans).casefold()

with open('./oz_cleaned.md','w') as file:
    file.write(text_cleaned)

# %%
