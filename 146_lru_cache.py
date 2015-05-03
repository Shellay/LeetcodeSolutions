class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
    def __repr__(self):
        return 'N{%s}' % self.value
    def chain_prev(self, prev):
        self.prev = prev
        prev.next = self
    def chain_next(self, next):
        self.next = next
        next.prev = self 
    def pump_out(self):
        self.prev.chain_next(self.next)
        return self

class Queue:

    def __init__(self, size):
        self.head = Node('HEAD')
        self.end = Node('END')
        self.head.chain_next(self.end)
        self.pool = {} # { key : Node }
        self.size = size
        self.counter = 0

    def __repr__(self):
        s = 'Q['
        q = self.head.next
        while q is not self.end:
            s += ' %s ' % q
            q = q.next
        return s + ']'

    def is_empty(self):
        return self.head.next is self.end

    # En/Dequeue are irrelavant to self.pool.
    def enqueue(self, value):
        n = Node(value)
        self.end.prev.chain_next(n)
        n.chain_next(self.end)
        self.counter += 1
        # Maintaining size.
        if self.counter > self.size:
            v = self.dequeue()
            print(v, ' is dequeued.')
            self.counter -= 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError('Empty queue') 
        else:
            n = self.head.next
            n.pump_out()
            return n.value

    def get(self, key):
        if key in self.pool:
            # Quick lookup.
            n = self.pool[key]
            # Append corresponding node to the end.
            n.pump_out()
            # Not destroy n.
            self.end.prev.chain_next(n)
            n.chain_next(self.end)
            return n.value
        else:
            raise KeyError 

    def set(self, key, value):
        if key in self.pool:
            # Now pool[key] is the node in the queue.
            # Only update its value, priority remains.
            self.pool[key].value = value
        else:
            self.enqueue(value)
            self.pool[key] = self.end.prev

inp = {
    'John' : 'Kansas',
    'Susi' : 'Carlifonia',
    'Mytho': 'Greek',
    'Pehta': 'Angola',
    'Yummi': 'Marz',
    'Puchi': 'Blues',
    'Gabi' : 'Saxon',
}

q = Queue(5)

for k,v in inp.items():
    q.set(k, v)

