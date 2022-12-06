s = open('day6_input.txt').read()

i = 3
while (len(set([s[i],s[i-1],s[i-2],s[i-3]])) < 4):
	i += 1
print(i+1)

i = 13
diff = 0
while diff < 14:
	l = []
	for c in range(14):
		l.append(s[i-c])
	diff = len(set(l))
	i += 1
print(i)