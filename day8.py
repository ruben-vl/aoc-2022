import numpy as np

input = np.array([[int(ch) for ch in row] for row in open('day8_input.txt').read().split('\n')])

def is_visible(row,col):
	return np.sum(np.array(input[row,col+1:]) >= input[row,col]) == 0\
		or np.sum(np.array(input[row,:col]) >= input[row,col]) == 0\
		or np.sum(np.array(input[:row,col]) >= input[row,col]) == 0\
		or np.sum(np.array(input[row+1:,col]) >= input[row,col]) == 0

result = [is_visible(int(row),int(col)) for row in range(len(open('day8_input.txt').read().split('\n')))
							  			for col in range(len(open('day8_input.txt').read().split('\n')[0]))]
print(sum(result))


# input = np.array([[1,2,3,4,3,4,3,2,1],[1,2,3]],dtype=object)

# def split(arr, cond):
#   return [arr[cond], arr[~cond]]

# def scenic_score(row,col):
# 	print(input)
# 	r = np.array(input[row,col+1:]) >= input[row,col]
# 	return len(split(r,r==True)[0])

# print(scenic_score(0,2))

