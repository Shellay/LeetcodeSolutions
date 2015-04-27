class Node(object):
    def __init__(self, label):
        self.label = label
        self.next = None
        self.other = None
    def __repr__(self):
        return 'N(%s)@%4s' % (self.label, id(self) % 10000)

def copy_deep(head): 
    lookup = {}                    # lookup :: id_num -> Node 
    def locate(n):
        if n is None:
            return None
        else:
            if id(n) not in lookup: 
                lookup[id(n)] = Node(n.label)
            return lookup[id(n)]
    #
    n = head
    m0 = locate(head)
    while n: 
        m = locate(n)
        m.next = locate(n.next)
        m.other = locate(n.other)
        n = n.next
    return m0 

n1 = Node('1')
n2 = Node('2')
n3 = Node('3')
n4 = Node('4')

n1.next, n1.other = n2, n4
n2.next, n2.other = n3, n1
n3.next, n3.other = n4, n4
n4.next, n4.other = None, n3

m1 = copy_deep(n1)

def print_nodes(n):
    while n:
        print(n, n.next, n.other)
        n = n.next
