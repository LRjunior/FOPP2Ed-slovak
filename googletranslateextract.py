import re
import codecs

filenamein = 'foppsk20151010.html'
filenameout = 'fopp20151010slovak.html'

fh = codecs.open(filenamein, 'r', 'utf-8')
data = fh.read()
fh.close()

f_out = codecs.open(filenameout+"aa", 'w', 'utf-8')
f_out.write(data)
f_out.close()

import re

myfile = codecs.open(filenamein, 'r', 'utf-8')
regex  = re.compile(r'<span.*?>(.*?)</span>',re.S|re.M) #re.compile(r'(?<b).*?(?b)')

f_out = codecs.open(filenameout, 'w', 'utf-8')


arr = []

for line in myfile:
    matches = regex.findall(line)
    
    for m in matches:
        arr.append(m.strip())

arrset = set(arr)
arr = list(arrset)
arr.sort()

for a in arr:
  if not a.startswith("<a"):
    f_out.write(a+"\n")

f_out.close()