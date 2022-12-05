with open('day5_input.txt') as f: 
	input = f.read().split('\n')

stacks = [
	['R','N','P','G'],
	['T','J','B','L','C','S','V','H'],
	['T','D','B','M','N','L'],
	['R','V','P','S','B'],
	['G','C','Q','S','W','M','V','H'],
	['W','Q','S','C','D','B','J'],
	['F','Q','L'],
	['W','M','H','T','D','L','F','V'],
	['L','P','B','V','M','J','F']
]

def move(amount, fro, to):
	fro -= 1
	to -= 1
	toMove = stacks[fro][-amount:]
	toMove.reverse() # TOGGLE COMMENT FOR PART 1/2
	stacks[fro] = stacks[fro][:len(stacks[fro])-amount]
	stacks[to] += toMove

input = map(lambda x: x.replace("move ","").replace(" from ", ";").replace(" to ", ";"),input)

for i in input:
	ii = i.split(";")
	move(int(ii[0]),int(ii[1]),int(ii[2]))

result = ""
for i in stacks:
	result += i[-1]
print(result)