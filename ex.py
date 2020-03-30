from nltk.tokenize import sent_tokenize

patch_text = r'D:\slava\example.txt'
path_write = r'D:\slava\writingf11129222222222.txt'

txt = open(patch_text).read() # open text
str2 = ''
for c in txt: # delete all bad simbols in text
    if c not in ('I', 'V', '...', '[', ']', '(', ')', '…', '..', '–', '!..', '\r', ', ,', ". .", '..', '\"'):
        str2 += c
str2 = str2.replace("\n", " ") #replace \n -> ' '
str2 = str2.replace("...", ".")
sents = sent_tokenize(str2) #tokenize
print(sents[0])
sentens = []
temple_str = ''
for sent in sents:
    opens = "«"
    close = "»"

    count_open = sent.count(opens)
    count_close = sent.count(close)
    if (count_open == 0 and count_close == 0) or (count_open == 1 and count_close == 1):
        sentens.append(sent)
    if count_close == 0:
        temple_str += sent
    elif count_close == 1:
        temple_str += sent
        sentens.append(temple_str)
        temple_str = ''
print(sentens[0])
a = 0
f = open(path_write, 'w')
for sent in sentens:# write to the file
    if len(sent) <= 200:
        f.write(sent + '\n')
        a += 1
print(a)
