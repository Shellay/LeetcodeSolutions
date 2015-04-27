# Suppose a sorted array is rotated at some pivot
# unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.
# *. O(logN) is required.

inp = [4,5,6,7,0,1,2,]
inp1 = [4,4,5,5,6,7,7,7,7,7,7,7,7,-1,0,1,2,2,4,]

def naive(inp):
    for i, j in enumerate(range(1, len(inp))):
        if inp[i] > inp[j]:
            return inp[j]
    return inp[-1]

# Divide and comquer...
# For rotated sorted array,
# Either its left half xor right half
# is monotonly increasing.
# The head must be greater than the end!!
# If the middle term is less than head, then search left half,
# otherwise search the right half.
def find_min(inp): 
    if len(inp) == 1:
        # return inp[0] 
        raise ValueError('Unexpected reach.')
    elif len(inp) == 2:
        return inp[1]
    else: 
        m = len(inp) // 2 
        if inp[m-1] > inp[m]:
            return inp[m]
        elif inp[m] > inp[m+1]:
            return inp[m+1]
        else:
            if inp[0] > inp[m]:
                return find_min(inp[:m])
            else:
                return find_min(inp[m+1:])
