#count a lot
import random

random.seed(0)

n = 10 #number of distinct elements in the universe
m = 15 #number of elements in the stream
stream = [2, 1, 2, 2, 3, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 3, 1, 1, 1, 1]#[random.randint(0,n) for i in range(m)]

class bin:

    def __init__(self, id):
        self.bin_no = id
        self.element = None
        self.counter = 0

    def __repr__(self):
        return "{'"+str(self.element) + "'->" + str(self.counter)+'}'


k = 2 #number of bins
bins = [bin(i) for i in range(k)]

history = {b.bin_no: [b.element] for b in bins}

def countalot(stream):
    for j, a in enumerate(stream):
        #print('Processing elem:', a, ' Currrent bins:', bins)
        for b in bins:
            if b.element == a:
                #print("Found a bin")
                b.counter += 1
                break
        else:
            minimum = bins[0].counter
            min_obj = bins[0]
            for b in bins:
                if b.counter < minimum:
                    minimum = b.counter
                    min_obj = b
            #print("Bin not found, incrementing bin:", min_obj)
            min_obj.element = a
            min_obj.counter += 1
            history[min_obj.bin_no].append(min_obj.element)
        print("i:", j, "a:", a, [(b.bin_no, b.element, b.counter) for b in bins])

def output(i):
    for b in bins:
        if b.element == i:
            return b.counter
    return 0

if __name__ == '__main__':
    print(stream)
    countalot(stream)
    print(bins)
    print(history)
    print(output(2))
