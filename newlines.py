import re
import codecs

filenamein = 'text.tex' #'zaklady_cvicenia_na_klaviri.tex'
filenameout = 'textout.tex'

fh = codecs.open(filenamein, 'r', 'utf-8')
data = fh.read()
fh.close()

lines = data.split("\n")

processed = ''
lineslen = len(lines)

par = False
for i,a in enumerate(lines):
	b = a.rstrip()
	#if i > 0:
	#	p = lines[i-1].rstrip()
	if True:	
		if len(b) > 0:
			if par:
				processed += ' ' + b
			else:
				processed += b
			par = True
		else:
			par = False
			processed += "\r\n\r\n"

f_out = codecs.open(filenameout, 'w', 'utf-8')

f_out.write(processed)

f_out.close()