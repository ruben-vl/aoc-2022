with open('day1_input.txt') as read_file: in_str = read_file.read()
print(max([sum(map(lambda x: int(x), i.split('\n'))) for i in in_str.split('\n\n')]))
print(sum(sorted([sum(map(lambda x: int(x), i.split('\n'))) for i in in_str.split('\n\n')],reverse=True)[0:3]))