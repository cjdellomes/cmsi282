def pair(input_list):
	pairs = []
	i = 0
	while i < len(input_list) - 1:
		pair = []
		pair.append(input_list[i])
		pair.append(input_list[i+1])
		i += 2
		pairs.append(pair)
	return pairs

def discard(input_list):
	for i in range(len(input_list)-1):
		if input_list[i][0] != input_list[i][1]:
			input_list.remove(input_list[i])
			i-1
		else:
			input_list[i].pop()
	return input_list

def recursive(input_list):
	new_list = []
	leftovers = pair(input_list)
	discard(leftovers)
	for i in leftovers:
		new_list.append(i[0])
	new_length = len(new_list)
	if new_length > 1:
		new_list = recursive(new_list)
	return new_list