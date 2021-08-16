import os, re
import codecs

def vlna(inputstring, replacement):
	return re.sub("[ ]" + replacement + "[ ]", " " + replacement + "\u00A0", inputstring)


filenamein = 'iii7.tex' #'zaklady_cvicenia_na_klaviri.tex'
filenameout = 'z.txt'

fh = codecs.open(filenamein, 'r', 'utf-8')
subject = fh.read()
fh.close()

s = subject

for r in ['a','i','k','o','s','so','u','v','vo','z','zo','A','I','O','S','V','Z']:
	s = vlna(s, r)

f_out = codecs.open(filenameout, 'w', 'utf-8')
f_out.write(s)
f_out.close()