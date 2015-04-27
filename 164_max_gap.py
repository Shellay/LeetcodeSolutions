import heapq
import random
import pprint
inp = [84, 93, 45, 36, 51, 16, 85, 20, 40, 53, 89, 4, 22, 35, 13, 54, 16, 95, 26, 0]
inp1 = [random.randint(0, 200) for _ in range(30)]
inpM = [random.randint(0, 10000) for _ in range(300)]

def naive(inp):
    inp = sorted(inp)
    return max(inp[i] - inp[i-1] for i in range(1, len(inp)))

class Buckets:
    def __init__(self, low, up, n):
        self.n = n
        self.low, self.up = low, up
        self.bkts = [[] for _ in range(n-1)] 
        self.delta = (up - low) / (n - 1)
    def __repr__(self):
        return 'Bucket[\nMIN:{0}\n{2}\nMAX:{1}]'.format(
            self.low, self.up, pprint.pformat(self.bkts))
    def __call__(self, num):
        if num < self.low or self.up < num:
            raise ValueError('Out of range.')
        i = int((num-self.low) // self.delta)
        return self.bkts[i]
    def _put(self, num): 
        heapq.heappush(self(num), num)
    def put(self, nums):
        for n in nums: self._put(n)
    @property
    def max_interval(self):
        intv = 0 ; u0 = self.low
        for i, bkt in enumerate(self.bkts):
            if bkt:
                l1, u1 = bkt[0], bkt[-1] 
                intv1 = l1 - u0
                if intv < intv1: intv = intv1
                u0 = u1 
        return intv

def make_buckets(inp):
    random.shuffle(inp)
    bk = Buckets(min(inp), max(inp), len(inp))
    bk.put(set(inp) - {max(inp), min(inp)})
    return bk

bk = make_buckets(inp)
bk1 = make_buckets(inp1)
bkM = make_buckets(inpM)

assert bk.max_interval == naive(inp)
assert bk1.max_interval == naive(inp1)
assert bkM.max_interval == naive(inpM)
