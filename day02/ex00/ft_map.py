
# lst = [1,2,4,5]
# memes = ["It's over 9000 !", "All your base are belong to us."]


# print(lst)
# print(memes)


# print(list(map(lambda a: a + 1, lst)))
# print(list(map(str.upper, memes)))


def ft_map(function_to_apply, list_of_inputs):
	return (function_to_apply(i) for i in list_of_inputs)


# print(list(ft_map(lambda a: a + 1, lst)))
# print(list(ft_map(str.upper, memes)))
# print((ft_map(str.upper, memes)))



