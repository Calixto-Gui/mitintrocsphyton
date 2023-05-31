import string

phrase = 'Purple COw green'
text = 'The Purple!!# $COW!green!! is*)() soft and cuddly'
# text_low = text.lower()
# punctuation = string.punctuation

# for c in punctuation:
#     text_low = text_low.replace(c,"")

# print(phrase in text_low)




text = text.lower()
phrase = phrase.lower()
punctuation = string.punctuation
        
for c in punctuation:
    text = text.replace(c," ")
            
text_lst = text.split()
phrase_lst = phrase.split()

t = any(phrase_lst == text_lst[i:i+len(phrase_lst)] for i in range(len(text_lst) -1))
            
print(t)