import time

def ft_progress(listy=None):
	for i in listy:
		yield i 


listy = range(1000)

ret = 0
for elem in ft_progress(listy):
 ret += (elem + 3) % 5
 # time.sleep(0.01)
print()
print(ret)