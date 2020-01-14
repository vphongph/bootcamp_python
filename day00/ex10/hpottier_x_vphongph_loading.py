import sys
import time
import subprocess as sp


def ft_progress(listy=100):
    st = time.time()
    for x in listy:
        progress = (x / listy[-1])
        block = int(progress * 25)
        ct = time.time() - st
        if (progress != 0):
            eta = (ct / progress) - ct
        else:
            eta = 0
        text = "ETA: {5:.2f}s [{0:>3}%] 8{1} {2:>" + str(len(str(listy[-1]))) + "}/{3} | elapsed time {4:.2f}s"
        text = text.format(int(progress * 100), "=" * block + ">" + " " * (25 - block), x, listy[-1], ct, eta)
        print(f"{text}", end = "")
        sys.stdout.flush()
        # sp.call('clear',shell=True)
        print("\b" * len(text), end = "")
        yield x

listy = range(1001)
ret = 0

for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.001)
print()
print(ret)
