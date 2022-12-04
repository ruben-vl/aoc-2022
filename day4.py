input = open('day4_input.txt').read().split('\n')

result = []
for row in input:
	rs = row.split(',')
	r1s = rs[0].split('-')
	r2s = rs[1].split('-')
	r1 = set(range(int(r1s[0]),int(r1s[1])+1))
	r2 = set(range(int(r2s[0]),int(r2s[1])+1))
	result += [r1.issubset(r2) or r2.issubset(r1)]
print(sum(result))

result = []
for row in input:
	rs = row.split(',')
	r1s = rs[0].split('-')
	r2s = rs[1].split('-')
	r1 = set(range(int(r1s[0]),int(r1s[1])+1))
	r2 = set(range(int(r2s[0]),int(r2s[1])+1))
	result += [len(r1.intersection(r2)) > 0]
print(sum(result))