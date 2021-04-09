from libindic.transliteration import getInstance
t = getInstance()
f = open('result.txt', 'r')
out = open('enresult.txt','w')
out.write('')
out.close()
out = open('enresult.txt','a')
for lines in f:
	text = lines.rstrip('\n')
	t_text = t.transliterate(text, "en_US")
	out.write(t_text+"\n")
	print(t_text) #"നമസ്കാര"
