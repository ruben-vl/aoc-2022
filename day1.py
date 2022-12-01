with open('day1_input.txt') as read_file:
	in_str = read_file.read()

sums = []
for i in in_str.split('\n\n'):
	sums += [sum(map(lambda x: int(x), i.split('\n')))]
print(max(sums))

sums.sort(reverse=True)

print(sum(sums[0:3]))