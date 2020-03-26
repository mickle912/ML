from nltk.tokenize import sent_tokenize


txt = open(r'D:\slava\example.txt').read()
str2=''
for c in txt:
   if c not in ('0','1','2','3','4','5','6','7','8','9', '—', 'I', '»', '«', 'V', '-', '...', '[', ']', '(', ')', '…', '..', '–', '!..', '“', '„', '\r', '\n', ', ,'):
      str2=str2+c
str2.replace(';', ',')
sents = sent_tokenize(str2, )
f = open(r'D:\slava\writingf14.txt', 'w')
for sents in sents:
  f.write(sents + '\n')