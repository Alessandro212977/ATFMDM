#prepro
#dist

          # w,  x,  y,  z
weights = [[0, 10, 20, 30], #w
           [10, 0, 10, 20], #x
           [20, 10, 0, 10], #y
           [30, 20, 10, 0]] #z

names = {'w': 0, 'x': 1, 'y': 2, 'z': 3}

A0 = {'w', 'x', 'y', 'z'}
A1 = {'w'}
A2 = set()

class Oracle:

    def __init__(self, A0, A1, A2):
        self.A0 = A0
        self.A1 = A1
        self.A2 = A2

        self.deltaA0 = {}
        self.deltaA1 = {}
        self.deltaA2 = {}
        self.p0 = {}
        self.p1 = {}
        self.B = {}

    def delta(self, A: set, v: str):
        return min([weights[names[elem]][names[v]] for elem in A])

    def p(self, A: set, v: str):
        for elem in A:
            if weights[names[elem]][names[v]] == self.delta(A, v):
                return elem
        else:
            raise AssertionError

    def bunch(self, v: str, dA1: dict, dA2: dict):
        result = set()
        for elem in A0-A1:
            if weights[names[elem]][names[v]] < dA1[v]:
                result.add(elem)
        for elem in A1-A2:
            if weights[names[elem]][names[v]] < dA2[v]:
                result.add(elem)
        return result

    def prepro(self):
        self.deltaA0 = {key: self.delta(self.A0, key) for key in names.keys()}
        self.deltaA1 = {key: self.delta(self.A1, key) for key in names.keys()}
        self.deltaA2 = {'w': 1e10, 'x': 1e10, 'y': 1e10, 'z': 1e10}

        self.p0 = {key: self.p(self.A0, key) for key in names.keys()}
        self.p1 = {key: self.p(self.A1, key) for key in names.keys()}

        self.B = {key: self.bunch(key, self.deltaA1, self.deltaA2) for key in names.keys()}

    def dist2(self, u: str, v: str):
        w = u
        i = 0
        if w not in self.B[v]:
            i += 1
            u, v = v, u
            w = self.p1[u]
        return weights[names[w]][names[u]]+weights[names[w]][names[v]]

test = Oracle(A0, A1, A2)
test.prepro()
print(test.dist2('y', 'x'))