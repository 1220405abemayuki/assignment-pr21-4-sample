# %%
with open('./oz.md','r') as file:
    text = file.read()

trans = str.maketrans(dict.fromkeys('#.,":;!',''))
text_cleaned = text.translate(trans).casefold()

with open('./oz_cleaned.md','w') as file:
    file.write(text_cleaned)

# %%
