from functools import reduce
print(sum(map(lambda x: x-96 if x > 96 else x-38,[ord(set(i[:len(i)//2]).intersection(i[len(i)//2:]).pop()) for i in open('day3_input.txt').read().split('\n')])))
print(sum(map(lambda x: x-96 if x > 96 else x-38,list(map(lambda x: ord(x.pop()), [reduce(lambda x,y: set(x)&set(y), sub) for sub in list(map(lambda *x: list(x), *([iter(open('day3_input.txt').read().split('\n'))] * 3)))])))))