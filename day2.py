with open('day2_input.txt') as read_file: in_str = read_file.read()
rounds = list(map(lambda x: x.replace(" ", ""), in_str.split('\n')))
points = {'AX': 3+1, 'AY': 6+2, 'AZ': 0+3, 'BX': 0+1, 'BY': 3+2, 'BZ': 6+3, 'CX': 6+1, 'CY': 0+2, 'CZ': 3+3}
print(sum(map(lambda x: points[x], rounds)))
new_points = {'AX': 0+3, 'AY': 3+1, 'AZ': 6+2, 'BX': 0+1, 'BY': 3+2, 'BZ': 6+3, 'CX': 0+2, 'CY': 3+3, 'CZ': 6+1}
print(sum(map(lambda x: new_points[x], rounds)))