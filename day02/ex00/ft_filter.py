
lst = ["It's over 9000 !", "All", ""]


# print(lst)
# print(memes)


print((filter(None, lst)))
# print(list(filter(lambda x: len(x) > 10, lst)))


def ft_filter(function_to_apply, list_of_inputs):
	if not function_to_apply:
		return (x for x in list_of_inputs if x)
	return (x for x in list_of_inputs if function_to_apply(x))


print((ft_filter(None, lst)))
# print(list(ft_filter(lambda x: len(x) > 10, lst)))
