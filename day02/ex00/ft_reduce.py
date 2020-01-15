from functools import reduce

# print(reduce(lambda a, b: a / b, range(1, 101)))

def ft_reduce(function_to_apply, list_of_inputs):

	new_x = list_of_inputs[0] 

	# MORE BLACK MAGIC, MORE PYTHONESQUE, MORE PYTHONISTIQUE
	# for x in list_of_inputs:
	# 	if list_of_inputs.index(x) == len(list_of_inputs) - 1:
	# 		break
	# 	new_x = function_to_apply(new_x, list_of_inputs[list_of_inputs.index(x) + 1])

	i = 1
	while i < len(list_of_inputs):
		new_x = function_to_apply(new_x, list_of_inputs[i])
		i += 1;

	return (new_x);

# print(ft_reduce(lambda a, b: a / b, range(1,101)))