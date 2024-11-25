'''Write a recursive function named linear that accepts the following arguments:

P: a non-empty list of positive integers
Q: a non-empty list of positive integers
k: a positive integer
It should return True only if both the conditions given below are satisfied:

P and Q are of same length.
P[i]=k⋅Q[i] for every integer i in the range [0,len(P)−1], endpoints inclusive.'''

def linear(P, Q, k):
    """
    A recursive function to determine if a list is scalar multiple of the other

    Arguments:
        P: list of integers
        Q: list of integers
        k: integer
    Return:
        result: bool
    """
    if not P and not Q:
        return True
    if len(P) != len(Q) or P[0] != k * Q[0]:
        return False
    return linear(P[1:], Q[1:], k)

''' Agar recursive nahi chahiye then yeh  code bhi kaam karna chahiye'''
    # flag = False
    # if len(P) == len(Q):
    #     for i in range(0, len(p)):
    #         if P[i] == k * q[i]:
    #             flag = True
    # return flag