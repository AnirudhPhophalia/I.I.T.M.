'''P is a dictionary of father-son relationships that has the following structure: for any key in the dictionary, its corresponding value is the father of key. As an example:

P = {
    'Jahangir': 'Akbar', 
    'Akbar': 'Humayun', 
    'Humayun': 'Babur'    
}

If 'Jahangir' is the key, then 'Akbar', his father, is the value. This is true of every key in the dictionary.
Write a recursive function named ancestry that accepts the following arguments:

P: dictionary of relationships
present: name of a person, string
past: name of a person, string
It should return the sequence of ancestors of the person named present, traced all the way back up to person named past. For example, ancestry(P, 'Jahangir', 'Babur') should return the list:

L = ['Jahangir', 'Akbar', 'Humayun', 'Babur']

In more Pythonic terms, L[i] is the father of L[i - 1], for 1≤i<len(L), with the condition that L[0] should be present and L[-1] should be past.
(1) You can assume that no two persons in the dictionary have the same name. However, a given person could either appear as a key or as a value in the dictionary.

(2) A given person could appear multiple times as one of the values of the dictionary. For example, in test-case-2, Prasanna has two sons, Mohan and Krishna, and hence appears twice (as a value).

(3) You do not have to accept input from the user or print output to the console. You just have to write the function definition.'''

def ancestry(P, present, past):
    """
    A recursive function to compute the sequence of ancestors of person

    Arguments:
        P: dict, key and value are strings
        present: string
        past: string
    Return:
        result: list of strings
    """
    if present == past:
        return [present]
    
    if present not in P:
        return []  # Return an empty list if 'present' is not in the dictionary.

    return [present] + ancestry(P, P[present], past)
