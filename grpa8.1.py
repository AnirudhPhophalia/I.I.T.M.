'''Write a recursive function named reverse that accepts a list L as argument and returns the reversed list.'''
def reverse(L):
    """
    A recursive function to reverse a list L

    Arguments:
        L: list, type of elements could be anything
    Return:
        result: list
    """
    if len(L) <= 1:
        return L

    # Recursive case: Reverse the rest of the list and append the first element at the end
    return reverse(L[1:]) + [L[0]]