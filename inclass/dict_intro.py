words = open('/usr/share/dict/words','r')
#words = ["z","zanier","zanies","zaniest","zaniness","zaniness's","zany","zany's","zap","zap's","zapped","zapping","zaps"]

combs = {}
for word in words:
	for i in range(1, len(word)-1):
		if word[0:i] in combs:
			combs[word[0:i]].append(word[i:len(word)].rstrip())
		else:
			combs[word[0:i]] = [word[i:len(word)].rstrip()]

for pre in combs:
	if len(pre) < 7:
		print pre + ":\t\t",
	else:
		print pre + ":\t",
	for suf in combs[pre]:
		print suf + " ",
	print "\n"

#print combs
