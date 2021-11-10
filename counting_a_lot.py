#count a lot
import random

n = 10 #number of distinct elements in the universe
m = 15 #number of elements in the stream
stream = [random.randint(0,n) for i in range(m)]

class bin:

    def __init__(self, id):
        self.bin_no = id
        self.element = None
        self.counter = 0


k = 3 #number of bins
bins = [bin(i) for i in range(k)]

def countalot(stream):
    for a in stream:
        pass
