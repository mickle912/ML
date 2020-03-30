from nltk.tokenize import sent_tokenize

patch_text = r'D:\slava\example.txt'
path_write = r'D:\slava\writingf101.txt'

txt = open(patch_text).read()
str2 = ''
for c in txt:
    if c not in ('I', 'V', '...', '[', ']', '(', ')', '…', '..', '–', '!..', '\r', ', ,', "»", "«"):
        str2 += c
str2 = str2.replace("\n", " ")
sents = sent_tokenize(str2)
f = open(path_write, 'w')
for sents in sents:
    sents = sents[:200]
    f.write(sents + '\n')
