from nltk.tokenize import sent_tokenize

patch_text = r'D:\slava\example.txt'
path_write = r'D:\slava\writingf12.txt'

txt = open(patch_text).read() # open text
str2 = ''
for c in txt: # delete all bad simbols in text
    if c not in ('I', 'V', '...', '[', ']', '(', ')', '…', '..', '–', '!..', '\r', ', ,', "»", "«"):
        str2 += c 
str2 = str2.replace("\n", " ") #replace \n -> ' '
sents = sent_tokenize(str2) #tokenize
f = open(path_write, 'w')
for sent in sents:# write to the file
    if len(sent) <= 200:
        f.write(sent + '\n')
