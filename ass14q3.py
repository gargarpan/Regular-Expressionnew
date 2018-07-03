import re
sentence = "A, very very; irregular_sentence"
s=re.sub('[\W _]',' ',sentence)
print(s)
